# avoid using TypedDict as it is deprecated


# from langchain_google_genai import ChatGoogleGenerativeAI
# from typing import TypedDict, Annotated, Optional, Literal
# from dotenv import load_dotenv

# load_dotenv()

# class Review(TypedDict):
#     summary: str
#     sentiment: str
#     pros: list[str]
#     cons: list[str]
#     author: str

# output_schema = {
#     "title": "Review",
#   "type": "object",
#   "properties": {
#     "key_themes": {
#       "type": "array",
#       "items": {
#         "type": "string"
#       },
#       "description": "Write down all the key themes discussed in the review in a list"
#     },
#     "summary": {
#       "type": "string",
#       "description": "A brief summary of the review"
#     },
#     "sentiment": {
#       "type": "string",
#       "enum": ["pos", "neg"],
#       "description": "Return sentiment of the review either negative, positive or neutral"
#     },
#     "pros": {
#       "type": ["array", "null"],
#       "items": {
#         "type": "string"
#       },
#       "description": "Write down all the pros inside a list"
#     },
#     "cons": {
#       "type": ["array", "null"],
#       "items": {
#         "type": "string"
#       },
#       "description": "Write down all the cons inside a list"
#     },
#     "name": {
#       "type": ["string", "null"],
#       "description": "Write the name of the reviewer"
#     }
#   },
#   "required": ["key_themes", "summary", "sentiment"]
# }

# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# structured_output = model.with_structured_output(output_schema)

# result = structured_output.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

# The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

# However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

# Pros:
# Insanely powerful processor (great for gaming and productivity)
# Stunning 200MP camera with incredible zoom capabilities
# Long battery life with fast charging
# S-Pen support is unique and useful
                                 
# Review by Vansh Thapar """)

# # print(result)
# print(result[0]["args"]["pros"])




# from langchain_google_genai import ChatGoogleGenerativeAI
# from typing import TypedDict, Literal, List, Optional
# import json
# from dotenv import load_dotenv

# load_dotenv()

# # 1️⃣ Define TypedDict for type hints
# class ProductReview(TypedDict):
#     name: str
#     summary: str
#     sentiment: Literal["positive", "negative", "neutral"]
#     rating: Optional[float]
#     pros: List[str]
#     cons: Optional[List[str]]
#     key_themes: List[str]
#     reviewer: Optional[str]

# # 2️⃣ Initialize the model
# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# # 3️⃣ Prompt for JSON output
# prompt = """
# Return a JSON object matching this format:
# {
#   "name": "string",
#   "summary": "string",
#   "sentiment": "positive | negative | neutral",
#   "rating": float or null,
#   "pros": ["list of pros"],
#   "cons": ["list of cons"] or null,
#   "key_themes": ["list of key themes"],
#   "reviewer": "optional name"
# }

# Review:
# "The Samsung Galaxy S24 Ultra is incredibly fast and has an amazing camera. 
# However, it is a bit heavy and expensive. Review by Vansh Thapar"
# """

# structured_output = model.with_structured_output(ProductReview)
# review: ProductReview = structured_output.invoke(prompt)

# print(review)


from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatGoogleGenerativeAI()

# schema
class Review(TypedDict):

    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]
    

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")

print(result['name'])