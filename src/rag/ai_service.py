import os
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain.tools import tool
from src.utils.tools import get_stock_price, get_company_info
from src.rag.rag import get_retriever

# Initialize the agent
agent_executor = None

@tool
def search_financial_report(query: str) -> str:
    """
    Searches and returns excerpts from the EasyFinance project report. 
    Use this to answer questions about the project itself, its features, or requirements.
    """
    retriever = get_retriever()
    if not retriever:
        return "Error: RAG system not initialized."
    
    docs = retriever.invoke(query)
    return "\n\n".join([doc.page_content for doc in docs])

def initialize_agent():
    global agent_executor
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Warning: OPENAI_API_KEY not found in environment variables.")
        return

    # 1. Setup LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # 2. Setup Tools
    tools = [get_stock_price, get_company_info, search_financial_report]

    # 3. Create Agent (using LangGraph)
    agent_executor = create_react_agent(llm, tools)

from langchain_community.llms import CTransformers
from langchain_core.prompts import PromptTemplate

# Global variable for local LLM
local_llm = None

def get_local_llm_response(query: str) -> str:
    global local_llm
    if local_llm is None:
        print("Loading Local LLM (Mistral 7B)...")
        try:
            local_llm = CTransformers(
                model="models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
                model_type="mistral",
                config={'max_new_tokens': 512, 'temperature': 0.7, 'context_length': 2048}
            )
        except Exception as e:
            return f"Error loading local model: {str(e)}"

    # Mistral Instruct format
    template = """<s>[INST] You are a helpful financial assistant named EasyFinance. Answer the user's question clearly and concisely.
{question} [/INST]"""
    prompt = PromptTemplate(template=template, input_variables=["question"])
    
    try:
        print(f"Generating response for: '{query}' (This may take over a minute)...")
        response = local_llm.invoke(prompt.format(question=query))
        print("Response generated.")
        return response
    except Exception as e:
        return f"Error generating response: {str(e)}"

def get_agent_response(query: str) -> str:
    # Direct Local Logic (Mistral 7B + Local Tools)
    lower_query = query.lower()
    
    # 1. Check for specific tools first (Rule-based routing)
    if "stock" in lower_query or "price" in lower_query:
        words = query.split()
        for word in words:
            if word.isupper() and len(word) <= 5:
                return f"[Local Tool] " + get_stock_price.invoke(word)
    
    if "company" in lower_query:
        words = query.split()
        for word in words:
            if word.isupper() and len(word) <= 5:
                return f"[Local Tool] " + get_company_info.invoke(word)

    if "easyfinance" in lower_query or "project" in lower_query or "report" in lower_query:
        return f"[Local RAG] Search Result:\n" + search_financial_report.invoke(query)
    
    # 2. If no tool matches, use Local LLM for general chat
    return get_local_llm_response(query)
