import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

st.header("Research Tool")

paper_input = st.selectbox("Select the research paper",["Attention is all you need","BERT: Pre-training of deep and Bidirectional Transformers","GPT 3: Language Models are few shot learners" , "Diffusion models beats GANs on image systhesis"])

style_input = st.selectbox("Select explanation style",["Beginner-Friendly" , "Technincal","Code-technical" , "Mathematical"])

length_input = st.selectbox("Select explanation length",["Short (1-2 paragraph)" , "Medium (3-5 paragraph)","Long (detailed explanation)"])

# this is the default prompt_template

# template = PromptTemplate(
#     template = """
#     Please summarize the research paper titled "{paper_input}" with the following
#     specifications:
#     Explanation Style: {style_input}
#     Explanation Length: {length_input}
#     1. Mathematical Details:
#     - Include relevant mathematical equations if present in the paper.
#     - Explain the mathematical concepts using simple, intuitive code snippets
#     where applicable.
#     2. Analogies:
#     - Use relatable analogies to simplify complex ideas.
#     If certain information is not available in the paper, respond with: "Insufficient
#     information available" instead of guessing.
#     Ensure the summary is clear, accurate, and aligned with the provided style and
#     length.
# """,
# input_variables=["paper_input" , "style_input" ,"length_input"],
# validate_template = True
# )

# if we want to make the prompt template reusable then we can create a seprate file for this and we can integreate it like this instead of writting the prompt template code again and again

template = load_prompt('template.json')

# prompt = template.invoke({
#     'paper_input' : paper_input,
#     'style_input': style_input,
#     'length_input':length_input
# })

model = GoogleGenerativeAI(model="gemini-2.5-flash")
if st.button("Summarize"):
    # in this chain we are saying first template then model
    chain = template | model
    # automatically the variables gets inserted in the template and that is send to the model in one invoke only other wise we have to write invoke 2 times one for adding the variables to the prompt template and then while invoking the model
    result = chain.invoke({
    'paper_input' : paper_input,
    'style_input': style_input,
    'length_input':length_input
})
    st.text_area("Result",result)