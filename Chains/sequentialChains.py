from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

class Story(BaseModel):
    title: str = Field(description="The title of the story")
    content: str = Field(description="The content of the story in 5 lines")

parser = PydanticOutputParser(pydantic_object=Story)

prompt1 = PromptTemplate(
    template = "Generate a short story about a {topic} in {style} style. \n {format_instructions}",
    input_variables = ["topic", "style"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

model = GoogleGenerativeAI(model = "gemini-2.5-flash")
# sequential chain
chain = prompt1 | model | parser

result = chain.invoke({"topic": "bravery", "style": "fantasy"})
print(format_instructions := parser.get_format_instructions())
print("-----")
print("-----")
print("-----")
print("-----")
print("-----")
print("-----")
print("-----")
print("-----")
print(result)
print("-----")
print(type(result))
print("-----")
print("-----")
print(result.title)
print("-----")
print("-----")
print(result.content)