from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
import streamlit as st

load_dotenv()

model1 = GoogleGenerativeAI(model = "gemini-2.5-flash")
model2 = GoogleGenerativeAI(model = "gemini-2.5-flash")


# prompt1 = PromptTemplate(
#     template="You are a concise educational assistant. "
#         "Write exactly 3 clear, factual bullet points as notes about the topic: {topic}. "
#         "Each line should be short, informative, and unique.",
#     input_variables=["topic"]
# )

# prompt2 = PromptTemplate(
#     template="Create exactly 3 multiple-choice questions (MCQs) on the topic: {topic}. "
#         "Each question must have 4 options (A–D) and clearly mention the correct answer below each question. "
#         "Use clean formatting like:\n\n"
#         "Q1. ...\nA)\nB)\nC)\nD)\nAnswer: ...",
#     input_variables=["topic"]
# )

# prompt3 = PromptTemplate(
#     template="Combine the following notes and MCQs into a short document under **20 lines**.\n\n"
#         "Notes:\n{notes}\n\n"
#         "MCQs:\n{mcqs}\n\n"
#         "Format it nicely with clear headings and bullet points.",
#     input_variables=["notes","mcqs"]
# )

# parser = StrOutputParser()

# parallel_chain = RunnableParallel({
#     'notes': prompt1 | model1 | parser,
#     'mcqs': prompt2 | model2 | parser,
# })



# final_topic = st.text_input("Enter the topic to get notes and mcqs")

# merge_chain = prompt3 | model1 | parser
# # result = merge_chain.invoke({"topic": final_topic})

# # if st.button("Get Results !"):
# #     result = final_chain.invoke({"topic" : final_topic})
# #     st.text_area(result)

# # if st.button("Get Notes and MCQs"):
# #     if final_topic.strip() == "":
# #         st.warning("Please enter a topic.")
# #     else:
# #         with st.spinner("Generating..."):
# #             final_chain = parallel_chain | merge_chain
# #             final_result = parallel_chain.invoke({**parallel_chain})
# #         st.text_area("Generated Content:", value=final_result, height=400)

# if st.button("Get Notes and MCQs"):
#     if final_topic.strip() == "":
#         st.warning("Please enter a topic.")
#     else:
#         with st.spinner("Generating..."):
#             # Step 1: generate notes and mcqs in parallel
#             parallel_output = parallel_chain.invoke({"topic": final_topic})
            
#             # Step 2: pass generated notes and mcqs to merge_chain
#             final_result = merge_chain.invoke(parallel_output)
        
#         st.text_area("Generated Content:", value=final_result, height=400)




prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()
