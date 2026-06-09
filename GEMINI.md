# GEMINI.md - Project Context

## Project Overview
This is a **Healthcare Monitoring AI Agent** designed to provide a digital health assistant through a conversational interface. It uses **Retrieval-Augmented Generation (RAG)** to provide grounded answers from medical documents and a suite of custom tools for health calculations and medication safety.

### Core Architecture
- **Frontend:** React (TypeScript) with Vite (`frontend/`). Supports toggleable Dark Mode (default).
- **Backend:** FastAPI (`backend/app.py`) serving the agent logic.
- **Agent:** Custom `SimpleHealthAgent` in `agents/health_agent.py` using `langchain-groq`.
- **LLM:** Groq-hosted `llama-3.3-70b-versatile`.
- **RAG System:** 
  - **Vector DB:** ChromaDB (`vectorstore/chroma_db`).
  - **Embeddings:** HuggingFace `sentence-transformers/all-MiniLM-L6-v2`.
- **Tools:** `fitness_tool.py`, `medical_tool.py`, `medication_tool.py`.

---

## Building and Running

### Prerequisites
- Python 3.13+
- Node.js & npm
- Groq API Key (stored in `.env`)

### Key Commands
- **Run Backend:**
  ```powershell
  python backend/app.py
  ```
- **Run Frontend:**
  ```powershell
  cd frontend
  npm run dev
  ```
- **Ingest New Documents:**
  ```powershell
  python vectorstore/vector_store.py
  ```

---

## Development Conventions

### Coding Standards
- **Clean Code Policy:** NO comments (#) or docstrings (""") are allowed in source files. All code must be self-explanatory and minimal.
- **Surgical Tool Usage:** The agent uses a manual loop in `invoke()` to ensure robustness. Tools must be decorated with `@tool(description="...")` to provide descriptions without using docstrings.
- **Safety First:** A strict **Emergency Protocol** is implemented in the system prompt. Life-threatening symptoms trigger an immediate emergency warning.
- **Formatting:** Agent is instructed to use Markdown tables for health metrics to ensure professional and readable output.
- **Disclaimer:** All AI responses must include a medical disclaimer.

### Project Structure
- `agents/`: Contains the agent logic (`health_agent.py`) and RAG pipeline (`rag_chain.py`).
- `backend/`: FastAPI server implementation (`app.py`).
- `frontend/`: React + TypeScript frontend application.
- `tools/`: Atomic functions decorated with `@tool` for the agent to consume.
- `vectorstore/`: Logic for document loading, splitting, and vector storage.
- `data/`: Placeholder for medical PDFs.

### Tech Stack Decisions
- **FastAPI:** High-performance backend for serving the AI agent.
- **React:** Interactive and responsive frontend for the chat interface.
- **Groq:** Chosen for ultra-fast inference speed. `llama-3.3-70b-versatile` is used for its superior tool-calling accuracy.
- **Local Embeddings:** Used to maintain data privacy and reduce API costs.
- **ChromaDB:** Local vector database (ignored by git to keep repo clean).

---

## Contextual Warnings
- **Tool Descriptions:** Do NOT use docstrings for tool descriptions; use the `description` parameter in the `@tool` decorator to stay compliant with the Clean Code Policy.
- **Python Version:** Running on Python 3.13.
- **State Management:** Session history is managed by the frontend (React) and passed to the backend API.
