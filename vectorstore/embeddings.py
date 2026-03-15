from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():
    """
    Returns the Embedding Model used for vector generation.
    """
    
    model_name = "sentence-transformers/all-MiniLM-L6-v2"

    embeddings = HuggingFaceEmbeddings(
        model_name=model_name        
    )
    
    return embeddings