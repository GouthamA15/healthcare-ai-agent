import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from vectorstore.retriever import get_retriever
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

GROQ_API = os.environ.get("GROQ_API_KEY")

def get_rag_chain():
    """
    Creates a RAG Pipeline using Grop LLM + Retriever
    """
    
    
    # Load Retriever
    retriever = get_retriever()
    
    #Initialize Groq LLM
    llm = ChatGroq(
        groq_api_key = GROQ_API,
        model_name="llama-3.1-8b-instant"
    )
    
    #Prompt Template
    prompt = ChatPromptTemplate.from_template(
        """
        You are a Healthcare Assistant.
        
        Use ONLY the context below to answer the question.
        If the answer is not in the context, Say "I don't know".
        
        Context:
        {context}
        
        Qusetion:
        {question}
        """
    )
    
    def rag_pipeline(query: str):
        #Step1: Retrieve Documents
        docs = retriever.invoke(query)
        
        #Step2: Combine context
        context = "\n\n".join([doc.page_content for doc in docs])
        
        #Step3: Format prompt
        final_prompt = prompt.format(
            context=context,
            question=query
        )
        
        #Step4: Get LLM response
        response = llm.invoke(final_prompt)
        
        return response.content
    
    return rag_pipeline
    