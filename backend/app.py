from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import sys
import os

# Ensure the parent directory is in the path so we can import agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.health_agent import get_health_agent
from langchain_core.messages import HumanMessage, AIMessage

app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    prompt: str
    history: List[ChatMessage]
    profile: Dict[str, Any]

agent = get_health_agent()

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Convert history to LangChain format
        langchain_history = []
        for msg in request.history:
            if msg.role == "user":
                langchain_history.append(HumanMessage(content=msg.content))
            elif msg.role == "assistant":
                langchain_history.append(AIMessage(content=msg.content))

        # Enhance input with profile data
        p = request.profile
        enhanced_input = f"I am a {p.get('age')} year old {p.get('gender')}, weight {p.get('weight')}kg, height {p.get('height')}cm. {request.prompt}"

        response = agent.invoke({
            "input": enhanced_input,
            "history": langchain_history
        })

        return {"output": response["output"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
