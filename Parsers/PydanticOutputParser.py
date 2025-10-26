from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

model = GoogleGenerativeAI(model = "gemini-2.5-flash")

class Person(BaseModel):
    name: str = Field(description="The person's full name")
    age: int = Field(gt = 18, description="The person's age in years, must be greater than 18")
    city: str = Field(description="The city where the person lives")

parser = PydanticOutputParser(pydantic_object=Person)

template1 = PromptTemplate(
    template = "Generate name, age and city of a fictional {place} person. \n {format_instructions}",
    input_variables = ["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = template1 | model | parser

result = chain.invoke({"place": "Indian"})

print(result)