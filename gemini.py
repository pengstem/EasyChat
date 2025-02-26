from google import genai
from google.genai import types
import talkwithgemini 
import os

model_list=["gemini-2.0-flash","gemini-2.0-pro-exp-02-05","gemini-2.0-flash-thinking-exp"]
output_length=[8192,8192,65536]
api_key = input("Need a Google API key? Get one at https://aistudio.google.com/apikey 😊\n"
                "If you've already added it to your environment variables, enter 'y'\n"
                "Please enter your Google API key: ")
if api_key.lower() == "y":
	api_key = os.environ.get("GOOGLE_API_KEY")
talking_model = input("Select a communication mode:\n1. Voice Chat\n2. Text Chat\n")
client = genai.Client()

if talking_model== "2":
	model_name=input("Select a Gemini model:\n1. gemini-2.0-flash\n2. gemini-2.0-pro-exp\n3. gemini-2.0-flash-thinking\n")
	if model_name not in ["1","2","3"]:
		print("Invalid selection. Please try again.")
		exit()
	selected_model_name = model_list[int(model_name) - 1] 
	needs_custom_instruction=input("Would you like to customize the system instruction? (y/n)\nDefault is 'You are a helpful assistant'. ")
	if needs_custom_instruction=="y":
		system_instruct = input("Enter your custom system instruction: ") or "You are a helpful assistant"
	else:
		system_instruct = "You are a helpful assistant"
elif talking_model== "1":
	model_name=1
	print("Note: Voice mode currently supports English input with text responses only, and uses the gemini-2.0-flash model by default.")
	selected_model_name = "gemini-2.0-flash-exp"
	# Add this line to ensure system_instruct is defined for voice mode
	system_instruct = "You are a helpful assistant"
else:
	print("Invalid selection. Please try again.")
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
	print("Type your message or type 'exit' to end the conversation.")
	while True: 	
		user_message = input("User 👨: ")
		if user_message.lower() == "exit":
			user_message = "Goodbye! Thanks for chatting."
			print("Assistant 🤖: ", end="", flush=True)
			response_stream = chat.send_message_stream(user_message)

			for chunk in response_stream:
				print(chunk.text, end="", flush=True)
			print() 
			print("Session ended. Have a great day!")
			break
		response_stream = chat.send_message_stream(user_message)
		print("Assistant 🤖: ", end="", flush=True)
		for chunk in response_stream:
			print(chunk.text, end="", flush=True)
		print() 

if __name__=="__main__":
	if talking_model == "2":
		text_talk()
	else:
		main = talkwithgemini.VoiceChat(api_key=api_key)
		talkwithgemini.asyncio.run(main.run())