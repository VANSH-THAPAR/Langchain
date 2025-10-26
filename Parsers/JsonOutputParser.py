from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

parser = JsonOutputParser()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

template1 = PromptTemplate(
    template = "send me the details about {subject} /n {formal_instructions}",
    input_variables = ["subject"],
    partial_variables={"formal_instructions": parser.get_format_instructions()}
)

# prompt = template1.format(subject="volleyball")

# result = model.invoke(prompt)

chain = template1 | model | parser

result = chain.invoke({"subject": "volleyball"})

print(result)