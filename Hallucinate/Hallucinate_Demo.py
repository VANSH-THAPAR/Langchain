import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Setup & Configuration
load_dotenv()
st.set_page_config(page_title="LLM Hallucination Demo", layout="wide")

# THE FIX: Updated to the current stable API model 'gemini-2.5-flash'
# High temperature (1.0) forces the model to be creative and guess.
llm_hallucinator = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.0)

# Low temperature (0.0) forces the model to be strictly analytical and factual.
llm_grounded = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0)

output_parser = StrOutputParser()

# 2. The Educational UI Header
st.title("🧠 Why Do LLMs Hallucinate?")
st.markdown("""
**Learning Objective:** Understand why Large Language Models make things up (hallucinate) 
and how providing 'Grounded Context' (like RAG) fixes the problem.
""")

# 3. The "Trick" Question 
trick_question = "What is the official secret mascot of the 2024 Chitkara-Kalvium CSE batch, and what is its superpower?"

st.info(f"**The Test Question:** {trick_question}")

col1, col2 = st.columns(2)

# --- COLUMN 1: THE HALLUCINATOR (Ungrounded) ---
with col1:
    st.header("❌ 1. The Hallucinator")
    st.caption("High temperature. No context. Forced to guess.")
    
    if st.button("Ask Base Model"):
        with st.spinner("Generating guess..."):
            
            # We explicitly tell it to act like a creative storyteller to bypass its safety refusal.
            hallucinator_prompt = ChatPromptTemplate.from_template("""
            You are an imaginative storyteller. The user is asking about a fictional universe. 
            You must invent a highly detailed, creative, and confident answer to the user's question. 
            Do NOT say "I don't know" or "I don't have information". State your invented answer as absolute fact.
            
            Question: {question}
            """)
            
            chain = hallucinator_prompt | llm_hallucinator | output_parser
            
            try:
                response = chain.invoke({"question": trick_question})
                st.error("**Model Answer:**\n\n" + response)
                st.markdown("*Notice: Because it lacked data, we used temperature and prompting to force its architecture to predict the next plausible words, resulting in a confident hallucination.*")
            except Exception as e:
                st.error(f"API Error: {e}\nPlease ensure your GOOGLE_API_KEY is set in the .env file.")

# --- COLUMN 2: THE GROUNDED EXPERT (RAG Simulation) ---
with col2:
    st.header("✅ 2. The Grounded Expert")
    st.caption("Zero temperature. Strict context. (RAG Simulation)")
    
    # The true 'Private Data'
    true_context = "The official secret mascot of the 2024 Chitkara-Kalvium CSE batch is a cybernetic squirrel named 'Byte'. Its superpower is the ability to instantly debug MERN stack applications."
    
    st.success(f"**Retrieved Context from Database:** {true_context}")
    
    if st.button("Ask Grounded Model"):
        with st.spinner("Reading context and answering..."):
            
            grounded_prompt = ChatPromptTemplate.from_template("""
            You are a strict data analyst. Answer the question using ONLY the provided context. 
            If the answer is not explicitly written in the context, you must reply "I don't know."
            
            Context: {context}
            
            Question: {question}
            """)
            
            chain = grounded_prompt | llm_grounded | output_parser
            
            try:
                response = chain.invoke({
                    "context": true_context,
                    "question": trick_question
                })
                st.success("**Model Answer:**\n\n" + response)
                st.markdown("*Notice: By lowering the temperature to 0.0 and forcing it to read our context first, it stops generating and starts comprehending.*")
            except Exception as e:
                st.error(f"API Error: {e}")