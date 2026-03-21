import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from vectorstore.embeddings import get_embedding_model


DATA_PATH = "data"
CHROMA_PATH = "vectorstore/chroma_db"


def load_documents():
    
    #Documents get stroed in this format:
    """
    [
        Document(page_content="This is the page data", metadata={"source":"pdf", "page": 1}),
        Document(page_content="This is the next page data", metadata={"source":"pdf", "page": 2})
    ]    
    """
    
    documents = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DATA_PATH, file))
            documents.extend(loader.load())

    return documents


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(documents)
    #Now chunks would look like this:
    """
    [
        Document(page_content="small piece of first page", metadata={"source":"pdf", "page": 1}),
        Document(page_content="second piece of first page", metadata={"source":"pdf", "page": 1}),
        Document(page_content="third piece of first page", metadata={"source":"pdf", "page": 1}),
        Document(page_content="forth piece of first page", metadata={"source":"pdf", "page": 1}),
        Document(page_content="small piece of second page", metadata={"source":"pdf", "page": 2})
    ]
    """
    
    
    return chunks


def create_vector_store():

    documents = load_documents()

    if not documents:
        raise ValueError("No PDF Documents were found in data folder")
    
    chunks = split_documents(documents)

    embedding_model = get_embedding_model()

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_PATH
    )

    vectordb.persist()

    print("Vector database created successfully")
    print(f"Loaded {len(documents)} documents")
    print(f"Created {len(chunks)} chunks")
    
    return vectordb


if __name__ == "__main__":
    create_vector_store()