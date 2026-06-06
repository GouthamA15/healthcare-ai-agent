from langchain_core.tools import tool
from agents.rag_chain import get_rag_chain

rag_pipeline = get_rag_chain()

@tool(description="Answer medical or healthcare-related questions using medical documents.")
def medical_info_tool(query: str) -> str :
    return rag_pipeline(query)
