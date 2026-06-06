from langchain.tools import tool
from agents.rag_chain import get_rag_chain

#Initialize RAG Pipeline once
rag_pipeline = get_rag_chain()

@tool
def medical_info_tool(query: str) -> str :
    """
    Use this tool to answer medical or healthcare-related questions.
    It retrieves information from medical documents and provides accurate answers.
    """
    
    return rag_pipeline(query)
    