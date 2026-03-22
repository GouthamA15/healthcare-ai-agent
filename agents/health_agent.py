import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

from tools.fitness_tool import calculate_bmi, calculate_bmr
from tools.medical_info_tool import get_medical_knowledge
from tools.medication_tool import check_drug_interaction, get_medication_info

load_dotenv()

class SimpleHealthAgent:
    def __init__(self):
        GROQ_KEY = os.environ.get('GROQ_API_KEY')
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            api_key=GROQ_KEY,
            temperature=0,
        )
        self.tools_list = [
            calculate_bmi, 
            calculate_bmr, 
            get_medical_knowledge, 
            check_drug_interaction, 
            get_medication_info
        ]
        self.tools_dict = {t.name: t for t in self.tools_list}
        self.llm_with_tools = self.llm.bind_tools(self.tools_list)
        
        self.system_prompt = """You are a helpful AI Health Assistant. 
        - If a user has a medical emergency, tell them to call 911 immediately.
        - Use the provided tools to answer questions.
        - Always include a medical disclaimer."""

    def invoke(self, input_data):
        user_input = input_data["input"]
        messages = [SystemMessage(content=self.system_prompt), HumanMessage(content=user_input)]
        
        for _ in range(5):
            ai_msg = self.llm_with_tools.invoke(messages)
            messages.append(ai_msg)
            
            if not ai_msg.tool_calls:
                return {"output": ai_msg.content}
            
            for tool_call in ai_msg.tool_calls:
                tool_name = tool_call["name"]
                tool_func = self.tools_dict.get(tool_name)
                if tool_func:
                    observation = tool_func.invoke(tool_call["args"])
                    messages.append(ToolMessage(content=str(observation), tool_call_id=tool_call["id"]))
                else:
                    messages.append(ToolMessage(content=f"Error: Tool {tool_name} not found.", tool_call_id=tool_call["id"]))
            
        return {"output": "I'm sorry, I couldn't complete your request in time."}

def get_health_agent():
    return SimpleHealthAgent()
