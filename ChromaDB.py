from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
import os

# 📁 Paths
data_folder = r"C:\Users\Downloads\data"  # Replace with your path
chroma_db_folder = r"C:\Users\Downloads\data"  # Replace with your path

# 📌 Embedding model
embedding = HuggingFaceEmbeddings(model_name="BAAI/bge-large-en-v1.5")

# 📥 Load only Markdown Files
md_loader = DirectoryLoader(
    data_folder,
    glob="**/*.md",
    show_progress=True
)
md_docs = md_loader.load()

# 🏷️ Auto-tag department from filename
filtered_docs = []
for doc in md_docs:
    filename = os.path.basename(doc.metadata.get("source", "unknown"))
    if "finance" in filename.lower():
        doc.metadata["department"] = "Finance"
    elif "marketing" in filename.lower():
        doc.metadata["department"] = "Marketing"
    elif "hr" in filename.lower():
        doc.metadata["department"] = "HR"
    elif "engineering" in filename.lower():
        doc.metadata["department"] = "Engineering"
    else:
        doc.metadata["department"] = "General"
    filtered_docs.append(doc)

# ✂️ Text splitting
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(filtered_docs)

# 💾 Save to Chroma
vectordb = Chroma.from_documents(
    documents=split_docs,
    embedding=embedding,
    persist_directory=chroma_db_folder
)

print("✅ Markdown documents embedded successfully.")
