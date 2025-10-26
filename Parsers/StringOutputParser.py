from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

template1 = PromptTemplate(
    template = "Tell me a joke about {subject}.",
    input_variables = ["subject"]
)

template2 = PromptTemplate(
    template="Explain me the joke {text}.",
    input_variables=["text"]
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"subject": "computers"})

print(result)