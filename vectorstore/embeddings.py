from langchain_community.embeddings import HuggingFaceEmbeddings
from functools import lru_cache

@lru_cache(maxsize=1)
def get_embedding_model():
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    
    model_kwargs={
        "device": "cpu"
    }
    
    encode_kwargs={
        "normalize_embeddings": True
    }
    
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    
    return embeddings
