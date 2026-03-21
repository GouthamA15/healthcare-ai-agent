from langchain_groq import ChatGroq
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int):
    """
    This Tool is designed to multiply two integers
    """
    return a + b


response = multiply.invoke({'a' :5, 'b' :10})
print(multiply.description)
print(response)
    