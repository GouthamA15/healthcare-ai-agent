from vectorstore.retriever import get_retriever

def test_rag():
    retriever = get_retriever()
    
    query = "What are the symptoms of diabetes?"
    
    print(f"\nQuery: {query}\n")
    print("Top Results:\n")
    
    results = retriever.invoke(query)
    
    for i, doc in enumerate(results, 1):
        print(f"{i}. {doc.page_content}")
        
        
if __name__ == "__main__":
    test_rag()