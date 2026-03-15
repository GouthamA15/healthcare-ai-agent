import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from vectorstore.embeddings import get_embedding_model


DATA_PATH = "data/medical_docs"
CHROMA_PATH = "vectorstore/chroma_db"


def load_documents():
    documents = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DATA_PATH, file))
            documents.extend(loader.load())

    return documents


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = text_splitter.split_documents(documents)
    return chunks


def create_vector_store():

    documents = load_documents()

    chunks = split_documents(documents)

    embedding_model = get_embedding_model()

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_PATH
    )

    vectordb.persist()

    print("Vector database created successfully")


if __name__ == "__main__":
    create_vector_store()