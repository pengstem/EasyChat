from websockets.legacy.client import WebSocketClientProtocol
import asyncio
import base64
import json
import os
import sys
import pyaudio
from rich.console import Console
from rich.markdown import Markdown
from websockets.asyncio.client import connect
from websockets.asyncio.connection import Connection
import dotenv

dotenv.load_dotenv()

# 基础配置
FORMAT = pyaudio.paInt16
CHANNELS = 1
SEND_SAMPLE_RATE = 16000
CHUNK_SIZE = 512

host = "generativelanguage.googleapis.com"
model = "gemini-2.0-flash-exp"

# 语音设置
pya = pyaudio.PyAudio()

class VoiceChat:
    def __init__(self, api_key=None):
        self.ws: WebSocketClientProtocol | Connection
        self.audio_out_queue = asyncio.Queue()
        self.running_step = 0
        self.paused = False
        self.console = Console()
        # Use provided API key or fall back to environment variable
        self.api_key = api_key if api_key else os.environ.get("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("API key is required. Please provide it or set GOOGLE_API_KEY environment variable.")
        

    async def startup(self):
        """初始化对话"""
        # 设置初始配置
        setup_msg = {
            "setup": {
                "model": f"models/{model}",
                "generation_config": {"response_modalities": ["TEXT"]},
            }
        }
        await self.ws.send(json.dumps(setup_msg))
        await self.ws.recv()

        # 发送初始提示
        initial_msg = {
            "client_content": {
                "turns": [
                    {
                        "role": "user",
                        "parts": [
                            {
                                "text": "let's talk!",
                            }
                        ],
                    }
                ],
                "turn_complete": True,
            }
        }
        await self.ws.send(json.dumps(initial_msg))
        
        current_response = []
        async for raw_response in self.ws:
            response = json.loads(raw_response)
            try:
                if "serverContent" in response:
                    parts = response["serverContent"].get("modelTurn", {}).get("parts", [])
                    for part in parts:
                        if "text" in part:
                            current_response.append(part["text"])
            except Exception:
                pass

            try:
                turn_complete = response["serverContent"]["turnComplete"]
                if turn_complete:
                    if current_response:
                        self.console.print("Connection established ✅", style="green")
                        text = "".join(current_response)
                        self.console.print(Markdown(text))
                        return
            except KeyError:
                pass

    async def listen_audio(self):
        """监听音频输入"""
        mic_info = pya.get_default_input_device_info()
        stream = pya.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=SEND_SAMPLE_RATE,
            input=True,
            input_device_index=mic_info["index"],
            frames_per_buffer=CHUNK_SIZE,
        )

        self.console.print("🎤 I'm listening, feel free to speak", style="yellow")

        while True:
            if self.paused:
                await asyncio.sleep(0.1)
                continue

            data = await asyncio.to_thread(stream.read, CHUNK_SIZE)
            if self.running_step > 1:
                continue

            # 音量检测
            audio_data = []
            for i in range(0, len(data), 2):
                sample = int.from_bytes(data[i:i+2], byteorder="little", signed=True)
                audio_data.append(abs(sample))
            volume = sum(audio_data) / len(audio_data)

            if volume > 200:  # 音量阈值，可根据需要调整
                if self.running_step == 0:
                    self.console.print("🎤 :", style="yellow", end="")
                    self.running_step += 1
                self.console.print("*", style="green", end="")
            await self.audio_out_queue.put(data)

    async def send_audio(self):
        """发送音频数据"""
        while True:
            if self.paused:
                await asyncio.sleep(0.1)
                continue

            chunk = await self.audio_out_queue.get()
            msg = {
                "realtime_input": {
                    "media_chunks": [
                        {
                            "data": base64.b64encode(chunk).decode(),
                            "mime_type": "audio/pcm",
                        }
                    ]
                }
            }
            await self.ws.send(json.dumps(msg))

    async def receive_audio(self):
        """接收和处理响应"""
        current_response = []
        async for raw_response in self.ws:
            if self.running_step == 1:
                self.running_step += 1

            response = json.loads(raw_response)
            try:
                if "serverContent" in response:
                    parts = response["serverContent"].get("modelTurn", {}).get("parts", [])
                    for part in parts:
                        if "text" in part:
                            current_response.append(part["text"])
                            self.console.print("-", style="blue", end="")
            except Exception:
                pass

            try:
                turn_complete = response["serverContent"]["turnComplete"]
                if turn_complete and current_response:
                    text = "".join(current_response)
                    
                    # 检查是否是控制命令
                    if "暂停对话" in text.lower():
                        self.paused = True
                        self.console.print("\n⏸ Conversation paused. Say 'Continue conversation' to resume", style="yellow")
                    elif "继续对话" in text.lower() and self.paused:
                        self.paused = False
                        self.console.print("\n🎵 Conversation resumed", style="green")
                    
                    # 显示响应
                    self.console.print("\n=============================================", style="yellow")
                    self.console.print(Markdown(text))

                    current_response = []
                    self.running_step = 0 if not self.paused else 2
            except KeyError:
                pass

    async def run(self):
        uri = f"wss://{host}/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent?key={self.api_key}"
        
        async with connect(uri) as ws:
            self.ws = ws
            self.console.print("Gemini Voice Chat", style="green", highlight=True)
            self.console.print("============================================", style="yellow")
            
            await self.startup()

            async with asyncio.TaskGroup() as tg:
                tg.create_task(self.listen_audio())
                tg.create_task(self.send_audio())
                tg.create_task(self.receive_audio())

                def check_error(task):
                    if task.cancelled():
                        return
                    if task.exception():
                        print(f"Error: {task.exception()}")
                        sys.exit(1)

                for task in tg._tasks:
                    task.add_done_callback(check_error)

if __name__ == "__main__":
    main = VoiceChat()
    asyncio.run(main.run())