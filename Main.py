from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os
import torch
from confidential_key import OPENROUTER_API_KEY

torch.classes.__path__ = []

# Environment Setup
os.environ["OPENAI_API_KEY"] = OPENROUTER_API_KEY  # Replace with your OpenRouter key
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# LLM
llm = ChatOpenAI(
    openai_api_key=os.environ["OPENAI_API_KEY"],
    base_url=OPENROUTER_BASE_URL,
    model="deepseek/deepseek-r1-0528:free"
)

# Vector DB + Embeddings
embedding = HuggingFaceEmbeddings(model_name="BAAI/bge-large-en-v1.5")
persist_directory = r"C:\Users\Downloads\data"  # Replace with your path
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
retriever = vectordb.as_retriever(search_kwargs={"k": 10})

# Prompt
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a secure internal AI assistant for a fintech company with multiple departments (Finance, HR, Marketing, Engineering, General).

Use the following context to answer the user's question clearly and concisely.
If the user's question falls outside their authorized department scope, respond with:
"You are not authorized to access this information."

Context:
{context}

Question:
{question}
"""
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt_template}
)

# FastAPI Setup
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    role: str
    question: str

@app.post("/chat")
def chat(req: ChatRequest):
    role_rules = {
        "Finance Team": "Access to finance only.",
        "Marketing Team": "Access to marketing only.",
        "HR Team": "Access HR only.",
        "Engineering Department": "Access to engineering only.",
        "Employee Level": "Access only to general only.",
        "C-Level Executives": "Full access to all engineering, finance, general, HR, marketing."
    }
    rule = role_rules.get(req.role, "Access restricted.")
    scoped_query = f"[Role: {req.role} – {rule}] {req.question}"
    result = qa_chain.invoke({"query": scoped_query})
    return {"answer": result.get("result", "No response.")}
