from tools.medical_tool import medical_info_tool
import warnings


warnings.filterwarnings("ignore")

def main():
    query = "What are symptoms of diabetes"
    
    result = medical_info_tool.invoke(query)
    
    print("\nQuery: ", query)
    print("\nAnswer:\n ", result)
    
if __name__ == "__main__":
    main()