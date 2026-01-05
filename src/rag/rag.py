import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Global variable to hold the vector store
vector_store = None

def initialize_rag():
    global vector_store
    
    # 1. Load the PDF
    # Path relative to this file: ../../../data/Final report EasyFinance.pdf
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(base_dir, "..", "..", "data", "Final report EasyFinance.pdf")
    
    if not os.path.exists(pdf_path):
        # Fallback to checking from current working directory
        if os.path.exists("data/Final report EasyFinance.pdf"):
            pdf_path = "data/Final report EasyFinance.pdf"
        else:
            print(f"Warning: {pdf_path} not found. RAG will be empty.")
            return

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # 2. Split text
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    # 3. Create Embeddings (using HuggingFace for local/free embeddings)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 4. Create Vector Store
    vector_store = FAISS.from_documents(texts, embeddings)
    print("RAG System Initialized with PDF content.")

def get_retriever():
    if vector_store is None:
        initialize_rag()
    
    if vector_store:
        return vector_store.as_retriever(search_kwargs={"k": 3})
    return None
