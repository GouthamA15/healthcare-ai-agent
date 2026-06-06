# GEMINI.md - Project Context

## Project Overview
This is a **Healthcare Monitoring AI Agent** designed to provide a digital health assistant through a conversational interface. It uses **Retrieval-Augmented Generation (RAG)** to provide grounded answers from medical documents and a suite of custom tools for health calculations and medication safety.

### Core Architecture
- **Agent:** Custom `SimpleHealthAgent` in `agents/health_agent.py` using `langchain-groq`.
- **LLM:** Groq-hosted `llama-3.3-70b-versatile` (Primary for robust tool calling).
- **Conversational Memory:** Agent maintains context of the last 10 messages for follow-up queries.
- **RAG System:** 
  - **Vector DB:** ChromaDB (`vectorstore/chroma_db`).
  - **Embeddings:** HuggingFace `sentence-transformers/all-MiniLM-L6-v2` (running locally).
  - **Data Source:** Medical PDFs in the `data/` folder.
- **Tools:** 
  - `fitness_tool.py`: BMI, BMR calculations and query-based fitness assessment.
  - `medical_tool.py`: RAG-based knowledge retrieval (uses `rag_chain.py`).
  - `medication_tool.py`: Drug interaction checks and general drug info.
- **Frontend:** Streamlit dashboard in `ui/streamlit_app.py`.

---

## Building and Running

### Prerequisites
- Python 3.13+
- Groq API Key (stored in `.env`)

### Key Commands
- **Install Dependencies:**
  ```powershell
  python -m pip install -r requirements.txt
  ```
- **Run Streamlit UI:**
  ```powershell
  python -m streamlit run ui/streamlit_app.py
  ```
- **Ingest New Documents:**
  ```powershell
  python vectorstore/vector_store.py
  ```
- **Test Components:**
  ```powershell
  python test_medical_tool.py
  python test_fitness_tool.py
  python test_medication_tool.py
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
- `tools/`: Atomic functions decorated with `@tool` for the agent to consume.
- `ui/`: Streamlit components.
- `vectorstore/`: Logic for document loading, splitting, and vector storage.
- `data/`: Placeholder for medical PDFs.

### Tech Stack Decisions
- **Groq:** Chosen for ultra-fast inference speed. `llama-3.3-70b-versatile` is used for its superior tool-calling accuracy.
- **Local Embeddings:** Used to maintain data privacy and reduce API costs.
- **ChromaDB:** Local vector database (ignored by git to keep repo clean).

---

## Contextual Warnings
- **Tool Descriptions:** Do NOT use docstrings for tool descriptions; use the `description` parameter in the `@tool` decorator to stay compliant with the Clean Code Policy.
- **Python Version:** Running on Python 3.13.
- **State Management:** Session history is managed by the UI layer (Streamlit) and passed to the agent's `invoke` method.
