from langchain_community.vectorstores import Chroma
from vectorstore.embeddings import get_embedding_model

CHROMA_PATH="vectorstore/chroma_db"

def get_retriever():
    vectordb = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_model()
    )
    
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    
    return retriever
