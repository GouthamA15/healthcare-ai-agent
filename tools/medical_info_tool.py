from langchain_core.tools import tool
from vectorstore.retriever import get_retriever

@tool
def get_medical_knowledge(query: str) -> str:
    retriever = get_retriever()
    docs = retriever.invoke(query)
    
    context = "\n\n".join([doc.page_content for doc in docs])
    
    return context
