"""Create a retriever using Chroma. Try modern `langchain_chroma` first,
fall back to older LangChain providers if the new package isn't installed.
"""
from vectorstore.embeddings import get_embedding_model

CHROMA_PATH = "vectorstore/chroma_db"


def _import_chroma():
    try:
        from langchain_chroma import Chroma
        return Chroma
    except Exception:
        pass

    try:
        from langchain_community.vectorstores import Chroma
        return Chroma
    except Exception:
        pass

    try:
        from langchain.vectorstores import Chroma
        return Chroma
    except Exception as e:
        raise ModuleNotFoundError(
            "No compatible Chroma vectorstore found. Please install `langchain-chroma` or `langchain-community`, e.g. `pip install langchain-chroma`"
        ) from e


def get_retriever():
    ChromaImpl = _import_chroma()

    vectordb = ChromaImpl(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_model()
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    return retriever
