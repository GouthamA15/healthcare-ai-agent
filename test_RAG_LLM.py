from agents.rag_chain import get_rag_chain

def main():
    rag = get_rag_chain()
    
    query = "What are symptoms of diabetes?"
    
    answer = rag(query)
    
    print("\nQuery: ", query)
    print("\nAnswer: ", answer)
    
    
if __name__ == "__main__":
    main()