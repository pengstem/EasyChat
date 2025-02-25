from google import genai
from google.genai import types
import talkwithgemini 

model_list=["gemini-2.0-flash","gemini-2.0-pro-exp-02-05","gemini-2.0-flash-thinking-exp"]
output_length=[8192,8192,65536]
api_key = input("If you don't have one, quietly get one from https://aistudio.google.com/apikey 😊\
				\nPlease enter your GOOGLE_API_KEY: ")
talking_model = input("Please choose your mode:\n1 Voice Communication\n2 Text Communication\n")
client = genai.Client()

if talking_model== "2":
	model_name=input("please select the google model you want to use:\n1 gemini-2.0-flash\
				  \n2 gemini-2.0-pro-exp\n3 gemini-2.0-flash-thinking\n")
	if model_name not in ["1","2","3"]:
		print("Invalid input, please try again")
		exit()
	selected_model_name = model_list[int(model_name) - 1] 
	needasysteminstruction=input("Do you need to add a system instruction? (y/n)\
							  \nThe default system instruction is 'you are a helpful assistant'")
	if needasysteminstruction=="y":
		system_instruct = input("please enter your system instruction:") or "you are a helpful assistant"
	else:
		system_instruct = "you are a helpful assistant"
elif talking_model== "1":
	print("have to remind you that the voice mode now only supports english input and reply in text,\
	   and by default it will use the gemini-2.0-flash model")
	selected_model_name = "gemini-2.0-flash-exp"

else:
	print("Invalid input, please try again")
	exit()

chat = client.chats.create(
    model=selected_model_name,
    config=types.GenerateContentConfig(
        system_instruction=system_instruct,
        max_output_tokens=output_length[int(model_name) - 1], 
        temperature=0.7,
        top_p=0.95,
    )
)

def text_talk():
	print("Please enter your question, or type 'exit' to quit.")
	while True: 	
		user_message = input("user🐗: ")
		if user_message.lower() == "exit":
			user_message = "i am leaving you now, bye😭!"
			print("Model🤖: ", end="", flush=True) # 准备开始流式输出，不换行
			response_stream = chat.send_message_stream(user_message) # 使用 chat.send_message_stream

			for chunk in response_stream: # 迭代流式响应
				print(chunk.text, end="", flush=True) # 逐 chunk 打印，不换行
			print() 
			print("Goodbye!")
			break

		print("Model🤖: ", end="", flush=True) # 准备开始流式输出，不换行
		response_stream = chat.send_message_stream(user_message) # 使用 chat.send_message_stream

		for chunk in response_stream: # 迭代流式响应
			print(chunk.text, end="", flush=True) # 逐 chunk 打印，不换行
		print() 

if __name__=="__main__":
	if talking_model == "2":
		text_talk()
	else:
		main = talkwithgemini.AudioLoop()
		talkwithgemini.asyncio.run(main.run())