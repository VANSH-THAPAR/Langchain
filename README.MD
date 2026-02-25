# 🚀 GenAI Engineering Playground

### **LLM • RAG • LangChain • Agents • Vector DBs • Hallucination Analysis**

<div align="center">

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/LangChain-Orchestration-0052CC?style=for-the-badge&logo=chainlink&logoColor=white" />
<img src="https://img.shields.io/badge/OpenAI-LLMs-412991?style=for-the-badge&logo=openai&logoColor=white" />
<img src="https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white" />
<img src="https://img.shields.io/badge/Streamlit-UI-E74C3C?style=for-the-badge&logo=streamlit&logoColor=white" />
<img src="https://img.shields.io/badge/ChromaDB-Vector_Store-8E44AD?style=for-the-badge" />

</div>

A complete **end-to-end GenAI Engineering Repository** showcasing practical, production-ready implementations of:

* **LLMs & Chat Models**
* **Embeddings**
* **Retrieval-Augmented Generation (RAG)**
* **ChromaDB Vector Stores**
* **Output Parsing**
* **Agents & Tools**
* **LangChain Chains (Sequential/Conditional/Parallel)**
* **Hallucination Analysis & RAG Grounding**
* **Streamlit UI Apps**

---

# ⭐ Overview

This repository is a **reference-grade GenAI engineering collection**, built while mastering LangChain, LLMs, embeddings, RAG pipelines, hallucination mitigation, and agents.

It includes complete working demos for:

* Chat-based LLM interactions
* RAG with PDF knowledge bases
* Embeddings + semantic search
* Structured output enforcement (JSON/Pydantic)
* Sequential / conditional / parallel chains
* Multi-tool agent workflows
* Hallucination vs Grounded RAG comparison demo
* Streamlit-powered GenAI apps

This is designed to match **enterprise AI engineering expectations**.

---

# 📂 Project Structure

```
📦 repo
 ┣ 📁 1.LLMS
 ┃ ┗ 📄 1.LLM_demo.py
 ┣ 📁 2.ChatModels
 ┃ ┣ 📄 1.ChatModel_demo.py
 ┃ ┗ 📁 3.EmbeddedModels
 ┃   ┗ 📄 1.embeddingModel_query.py
 ┣ 📁 Chains
 ┃ ┣ 📄 sequentialChains.py
 ┃ ┣ 📄 conditionalChains.py
 ┃ ┗ 📄 parallelChains.py
 ┣ 📁 Chatbot
 ┃ ┗ 📄 Chatbot_program.py
 ┣ 📁 Parsers
 ┃ ┣ 📄 JsonOutputParser.py
 ┃ ┣ 📄 PydanticOutputParser.py
 ┃ ┗ 📄 StringOutputParser.py
 ┣ 📁 RAG
 ┃ ┣ 📁 dir_pdf
 ┃ ┣ 📁 document_loader
 ┃ ┃ ┣ 📄 DocumentLoader.py
 ┃ ┃ ┣ 📄 PDFLoader.py
 ┃ ┃ ┗ 📄 directory_loader.py
 ┃ ┣ 📁 Text_Splitter
 ┃ ┗ 📄 dock.txt, CSSNotesForProfessionals.pdf
 ┣ 📁 vectorStores
 ┃ ┗ 📄 chromadb.py
 ┣ 📁 Hallucinate
 ┃ ┗ 📄 Hallucinate_Demo.py
 ┣ 📁 Streamlit
 ┣ 📁 Structured_Output
 ┣ 📄 requirements.txt
 ┗ 📄 README.md
```

---

# 🧠 Key Features

## **1️⃣ LLMs & Chat Models**

* OpenAI / HuggingFace / Google Gemini integrations
* Chat-based interfaces
* Prompt templates, system messages
* Temperature + token control

---

## **2️⃣ Embeddings + Vector Stores**

* Embedding generation
* Semantic search
* ChromaDB integration
* Document chunk indexing

---

## **3️⃣ RAG (Retrieval-Augmented Generation)**

* PDF & directory loaders
* Text chunking / splitting
* Embedding-based retrieval
* Context-aware answering

---

## **4️⃣ Hallucination Demonstration (NEW 🔥)**

📁 `Hallucinate/Hallucinate_Demo.py`

An interactive Streamlit teaching artifact that demonstrates:

### 🧪 Why LLMs Hallucinate

**Column 1 – "The Hallucinator"**

* Temperature = 1.0
* Prompted to confidently guess fake facts
* Shows how probabilistic generation fabricates answers

**Column 2 – "The Grounded Expert"**

* Temperature = 0.0
* Uses strict context constraints
* Simulates RAG-style grounded answering

### ⚙ Tech Used

* Streamlit
* LangChain
* Google Gemini (`gemini-2.5-flash`)

This demo visually explains the **core engineering reason behind hallucinations** and how **RAG solves it** by grounding generation in retrieved context.

---

## **5️⃣ Chains (LangChain Core)**

* **Sequential Chains** → step-by-step reasoning
* **Conditional Chains** → logic-based branching
* **Parallel Chains** → simultaneous execution

---

## **6️⃣ Agents**

* Tool-enabled reasoning
* Multi-step automated workflows
* Self-directed decision loops

---

## **7️⃣ Output Parsing**

* JSON output parser
* String parser
* Pydantic typed structures

---

## **8️⃣ Streamlit UI**

* Interactive apps for LLM, RAG, and Hallucination demos
* Clean side-by-side comparison layouts
* Engineering-focused visualization

---

# ⚙️ Tech Stack

### **Languages**

* Python

### **Frameworks / Libraries**

* LangChain
* OpenAI
* Google Gemini
* HuggingFace
* ChromaDB
* Streamlit
* PyPDF

### **Concepts Covered**

* Prompt Engineering
* RAG Architecture
* Embeddings
* Vector Databases
* Hallucination Mitigation
* Grounded Generation
* Agent Orchestration

---

# 🏗️ How to Run

## **1. Clone Repository**

```bash
git clone <repo-url>
cd repo
```

---

## **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## **3. Add Environment Variables**

Create `.env`:

```
OPENAI_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
```

---

## **4. Run Any Python Script**

```bash
python 1.LLMS/1.LLM_demo.py
```

---

### 🔍 Test RAG Pipeline

```bash
python vectorStores/chromadb.py
```

---

## **5. Run Streamlit Apps**

### Main Streamlit App

```bash
streamlit run Streamlit/app.py
```

### 🧠 Run Hallucination Demo

```bash
streamlit run Hallucinate/Hallucinate_Demo.py
```

---

# 🎯 Real-World Use Cases

You can extend this repo into:

* Enterprise RAG chatbots
* Knowledge assistants
* Document intelligence systems
* Hallucination testing frameworks
* Automation agents for workflows
* Microservice-based AI systems

---

# ⭐ Why This Repo Stands Out

* Production-grade folder structure
* Covers **ALL** core GenAI engineering components
* Demonstrates embeddings, retrieval, parsing, AND hallucination mitigation
* Side-by-side hallucination vs grounded comparison
* Agent workflows for real automation
* Streamlit UI for demos
* Perfect for **AI Engineer roles**

---

# 📌 Future Enhancements

* LangGraph workflows
* FastAPI backend for RAG
* Automated hallucination evaluation benchmarks
* More vector DB options (FAISS, Pinecone)
* Model comparison dashboards

---

# 🤝 Contributions

Pull requests and suggestions welcome.

---

# 📞 Contact

Developed by **Vansh**

**Email:** *[vanshthapar.professional@gmail.com](mailto:vanshthapar.professional@gmail.com)*

---

### ⭐ If you like this project, please star the repository!
