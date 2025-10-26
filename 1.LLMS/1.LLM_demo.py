from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model = "gemini-2.5-pro")

result = llm.invoke("What is the captial of india")

print(result)