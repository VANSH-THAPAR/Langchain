from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.5-flash")

class Feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description="Give me the sentiment of the feedback")

parser = StrOutputParser()

pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)

prompt = PromptTemplate(
    template="Tell me the sentiment of the {message} either positive or negative \n {format_instructions} ",
    input_variables=["message"],
    partial_variables = {"format_instructions" : pydantic_parser.get_format_instructions()}
)

prompt_Positive = PromptTemplate(
    template = ("Reply in 2-3 lines to this positive feedback. "
        "Do NOT give multiple replies, options, or a list. "
        "Just give ONE natural, friendly response: {message}"),
    input_variables = ["message"]
)

prompt_Negative = PromptTemplate(
    template = ("Reply in 2-3 to this negative feedback. "
        "Do NOT give multiple replies, options, or a list. "
        "Just give ONE empathetic, friendly response: {message}"),
    input_variables=["message"]
)

classifier_chain = prompt | model | pydantic_parser

branch_chain = RunnableBranch(
    (lambda x : x.sentiment == "positive", prompt_Positive | model | parser ) ,
    (lambda x : x.sentiment == "negative", prompt_Negative | model | parser ),
    RunnableLambda(lambda x : "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({"message": "This is a bad phone"}))