import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

GROQ_KEY = os.environ.get('GROQ_API_KEY')
print(GROQ_KEY)


#Initializing LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=GROQ_KEY,
    temperature=0.2,
    max_tokens=600,
    model_kwargs={
        "top_p": 0.9,
        "frequency_penalty": 1.0,
        "presence_penalty": 0.1
    }
)

# Running basic prompt
response = llm.invoke("What is an AI Agent")

print('Response: ', response.content)