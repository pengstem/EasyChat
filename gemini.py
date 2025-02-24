from google import genai
import talkwithgemini 

model_list=["gemini-2.0-flash","gemini-2.0-pro-exp-02-05","gemini-2.0-flash-thinking-exp"]
api_key = input("If you don't have one, quietly get one from https://aistudio.google.com/apikey 😊\
				\nPlease enter your GOOGLE_API_KEY: ")
talking_mode = input("Please choose your mode:\n1 Voice Communication\n2 Text Communication\n")
client = genai.Client()

if talking_mode== "2":
	model_name=input("please select the google model you want to use:\n1 gemini-2.0-flash\n\
				  2 gemini-2.0-pro-exp\n3 gemini-2.0-flash-thinking\n")
else :
	print("have to remind you that the voice mode now only supports english input and reply in text,\
	   and by default it will use the gemini-2.0-flash model")

def text_talk():
	response = client.models.generate_content_stream(
    	model="gemini-2.0-flash",
    	contents=["Explain how AI works"])
	for chunk in response:
		print(chunk.text, end="")
	pass

if __name__=="__main__":
	text_talk()
	pass
