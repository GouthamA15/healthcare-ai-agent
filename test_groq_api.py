import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def test_groq():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("❌ Error: GROQ_API_KEY not found in .env file.")
        return

    client = Groq(api_key=api_key)
    
    print("--- Testing Groq API Connection ---")
    try:
        models = client.models.list()
        print("\n✅ Successfully connected! Available models:")
        for model in models.data:
            print(f"- {model.id}")
            
        print("\n--- Testing Completion with llama-3.3-70b-versatile ---")
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say hello!",
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        print(f"✅ Success! Response: {chat_completion.choices[0].message.content}")
        
    except Exception as e:
        print(f"❌ API Test Failed: {str(e)}")

if __name__ == "__main__":
    test_groq()
