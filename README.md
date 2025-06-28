# 💼 Fintech Role-Based AI Assistant using RAG  
**Secure, Smart & Department-Aware Knowledge Access**  
Built for the [Codebasics GenAI Resume Challenge](https://codebasics.io)

---

## 🚀 Overview

This project demonstrates how to build a **secure, internal AI assistant** for fintech enterprises using **LLMs + RAG (Retrieval-Augmented Generation)** and role-based access control.

Users can ask natural language questions and receive answers sourced from internal documents — filtered dynamically by **user role** (Finance, HR, Marketing, Engineering, etc.).

---

## 📌 Key Features

- 🔐 **Role-based document retrieval** (e.g., HR sees HR docs only)
- 🤖 **LLM-powered assistant** using DeepSeek + HuggingFace Embeddings
- 🗂️ **Vectorized document retrieval** via ChromaDB
- 🧠 **LangChain pipeline** for loading, splitting, tagging & embedding
- 🖥️ **Streamlit chat UI** with login, history & logout
- ⚙️ **FastAPI backend** handling secure prompt injection & responses

---

## 🛠️ Tech Stack

| Tool         | Purpose                            |
|--------------|-------------------------------------|
| `LangChain`  | Document orchestration & retrieval |
| `ChromaDB`   | Vector database for fast search     |
| `HuggingFace`| Embedding model (`bge-large-en-v1.5`) |
| `DeepSeek`   | LLM for accurate answers            |
| `FastAPI`    | Role-aware backend API              |
| `Streamlit`  | Frontend interface for users        |

---

## 🧩 Project Structure

📦fintech-rag-assistant/
├── app/ # FastAPI backend logic
├── ui/ # Streamlit interface
├── csv_to_md_converter.py # CSV to Markdown
├── ChromaDB.py # ChromaDB embeddings
├── main.py # FastAPI entrypoint
├── Streamlit_Chatbot_UI.py # Streamlit entrypoint
├── confidential_key.py # API key file (excluded in .gitignore)
└── README.md


---

## 🧪 How It Works

### 🔁 Step 1: Convert Department CSVs → Markdown

```bash
csv_to_md_converter.py

Converts HR CSVs to Markdown format

Automatically tags documents by department

Embeds them into ChromaDB for fast semantic search

🧠 Step 2: Role-Based Retrieval using FastAPI

uvicorn main:app --reload

Injects user role into prompt template

Validates access permissions per query

Prevents unauthorized retrieval:

"You are not authorized to access this information."

💬 Step 3: Interact via Streamlit UI

streamlit run Streamlit_Chatbot_UI.py

Login using static credentials for demo purposes

Login role (HR, Finance, CEO, etc.)

Ask document-based questions in natural language

🧑‍💻 Demo Roles & Access Matrix
🧑‍🤝‍🧑 Role 	      🔐 Access Scope
fin_user	      Finance documents only
hr_user	        HR documents only
mark_user	      Marketing documents only
eng_user	      Engineering documents only
emp_user	      General info only
ceo_user	      Full access to all departments

Use password 1234 for all users.

📷 Screenshot

<img width="959" alt="image" src="https://github.com/user-attachments/assets/9f15ea73-5f4f-41ae-bb80-32bb9a616564" />

🔒 Security Highlights

Scoped prompt injection ensures role-restricted answers

Backend validates every query with user metadata

Clean separation between interface, logic, and data access

📎 Prerequisites

Python 3.9+

Install dependencies:

pip install -r requirements.txt

# confidential_key.py

OPENROUTER_API_KEY = "paste-your-key-here"


✅ requirements.txt

# Core Dependencies
pandas
os
requests

# FastAPI Backend
fastapi
uvicorn
pydantic
python-multipart

# LangChain + Vector DB
langchain
langchain-community
langchain-core
langchain-openai
langchain-chroma
langchain-huggingface
chromadb

# Embeddings & Models
torch
sentence-transformers
transformers

# Streamlit Frontend
streamlit

# CORS Support
fastapi[all]


🙌 Credits
Built by Zaifudeen
AI Enthusiast | Workflow Automation Strategist
Part of the Codebasics GenAI Resume Challenge

📩 Connect on LinkedIn
🤝 Let's build secure and scalable internal AI tools together!


