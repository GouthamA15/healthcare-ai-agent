from functools import lru_cache
import os


def _import_hf_embeddings_class():
    """Try to import HuggingFaceEmbeddings from several possible packages.

    This avoids hard failures when the newer `langchain-huggingface` package
    isn't installed.
    """
    try:
        from langchain_huggingface import HuggingFaceEmbeddings

        return HuggingFaceEmbeddings
    except Exception:
        pass

    try:
        from langchain_community.embeddings import HuggingFaceEmbeddings

        return HuggingFaceEmbeddings
    except Exception:
        pass

    try:
        from langchain.embeddings import HuggingFaceEmbeddings

        return HuggingFaceEmbeddings
    except Exception as e:
        raise ModuleNotFoundError(
            "No compatible HuggingFaceEmbeddings found. Install `langchain-huggingface` or `langchain-community`"
        ) from e

@lru_cache(maxsize=1)
def get_embedding_model():
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    
    model_kwargs={
        "device": "cpu"
    }
    
    encode_kwargs={
        "normalize_embeddings": True
    }
    hf_token = os.environ.get("HF_TOKEN")

    init_kwargs = {
        "model_name": model_name,
        "model_kwargs": model_kwargs,
        "encode_kwargs": encode_kwargs,
    }

    if hf_token:
        init_kwargs["huggingfacehub_api_token"] = hf_token

    EmbeddingsClass = _import_hf_embeddings_class()
    embeddings = EmbeddingsClass(**init_kwargs)
    
    return embeddings
