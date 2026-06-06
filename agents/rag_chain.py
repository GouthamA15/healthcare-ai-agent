import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from vectorstore.retriever import get_retriever
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

GROQ_API = os.environ.get("GROQ_API_KEY")

def get_rag_chain():
    retriever = get_retriever()
    
    llm = ChatGroq(
        groq_api_key=GROQ_API,
        model_name="llama-3.3-70b-versatile"
    )
    
    prompt = ChatPromptTemplate.from_template(
        "You are a Healthcare Assistant.\n\n"
        "Use ONLY the context below to answer the question.\n"
        "If the answer is not in the context, Say \"I don't know\".\n\n"
        "Context:\n{context}\n\n"
        "Question:\n{question}"
    )
    
    def rag_pipeline(query: str):
        docs = retriever.invoke(query)
        context = "\n\n".join([doc.page_content for doc in docs])
        final_prompt = prompt.format(context=context, question=query)
        response = llm.invoke(final_prompt)
        return response.content
    
    return rag_pipeline
