from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

model = GoogleGenerativeAI(model = 'gemini-1.5-flash')

chat_history = [
    SystemMessage(content = 'you are a helpful assistant')
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if(user_input.lower() == "exit"):
        break
    else:
        chatbot_output = model.invoke(chat_history)
        chat_history.append(AIMessage(content = chatbot_output))
        print(chatbot_output)

print(chat_history)