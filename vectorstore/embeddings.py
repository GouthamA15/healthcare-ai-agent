from langchain_community.embeddings import HuggingFaceEmbeddings
from functools import lru_cache

@lru_cache(maxsize=1)
def get_embedding_model():
    """
    Loads and returns the embedding model.
    Uses caching to prevent reloading the model multiple times
    """
    
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    
    #Device Configuration (CPU for Now)
    model_kwargs={
        "device": "cpu"
    }
    
    #Encoding Configuration 
    encode_kwargs={
        "normalize_embeddings": True
    }
    
    #Initializing embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    
    return embeddings
    