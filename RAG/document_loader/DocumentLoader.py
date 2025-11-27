from json import load
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

prompt = PromptTemplate(
    template="Tell me a short summary of the following text:\n\n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()
loader = TextLoader("RAG/dock.txt")

docs = loader.load()

chain = prompt | model | parser

# print(docs)

result = chain.invoke({"text": docs[0].page_content})

print(result)