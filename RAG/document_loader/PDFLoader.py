from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

loader = PyPDFLoader("RAG/dock_pdf.pdf")

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Provide a concise summary of the following PDF content:\n\n{text}",
    input_variables=["text"]
)

docs = loader.load()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

chain = prompt | model | parser

result = chain.invoke({"text": docs[0].page_content})
print(result)
