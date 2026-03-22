from langchain_community.vectorstores import Chroma
from vectorstore.embeddings import get_embedding_model

db = Chroma(
    persist_directory="vectorstore/chroma_db",
    embedding_function=get_embedding_model()
)

results = db.similarity_search("diabetes symptoms", k=2)

for r in results:
    print(r.page_content)