# GEMINI.md - Project Context

## Project Overview
This is a **Healthcare Monitoring AI Agent** designed to provide a digital health assistant through a conversational interface. It uses **Retrieval-Augmented Generation (RAG)** to provide grounded answers from medical documents and a suite of custom tools for health calculations and medication safety.

### Core Architecture
- **Agent:** Custom `SimpleHealthAgent` in `agents/health_agent.py` using `langchain-groq`.
- **LLM:** Groq-hosted `llama-3.3-70b-versatile` or `llama-3.1-8b-instant`.
- **RAG System:** 
  - **Vector DB:** ChromaDB (`vectorstore/chroma_db`).
  - **Embeddings:** HuggingFace `sentence-transformers/all-MiniLM-L6-v2` (running locally).
  - **Data Source:** Medical PDFs in the `data/` folder.
- **Tools:** 
  - `fitness_tool.py`: BMI and BMR calculations.
  - `medical_info_tool.py`: RAG-based knowledge retrieval.
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
- **Test API Connection:**
  ```powershell
  python test_groq_api.py
  ```

---

## Development Conventions

### Coding Standards
- **Clean Code Policy:** NO comments (#) or docstrings (""") are allowed in source files. All code must be self-explanatory and minimal.
- **Surgical Tool Usage:** When using tool-calling with Groq, the agent uses a manual loop in `invoke()` to ensure robustness against parsing errors.
- **Safety First:** A strict **Emergency Protocol** is implemented in the `SimpleHealthAgent` system prompt. Any mention of life-threatening symptoms must trigger an immediate emergency warning before any tool use.
- **Disclaimer:** All AI responses must include a medical disclaimer.

### Project Structure
- `agents/`: Contains the agent logic and state management.
- `tools/`: Atomic functions decorated with `@tool` for the agent to consume.
- `ui/`: Streamlit components.
- `vectorstore/`: Logic for document loading, splitting, and vector storage.
- `data/`: Placeholder for medical PDFs.

### Tech Stack Decisions
- **Groq:** Chosen for ultra-fast inference speed, critical for conversational agents.
- **Local Embeddings:** Used to maintain data privacy and reduce API costs.
- **ChromaDB:** Used for its simplicity as a local vector database.
- **Vanilla CSS:** Preferred for Streamlit styling.

---

## Contextual Warnings
- **Groq Tool Parsing:** Be aware that Groq sometimes attempts to call tools using an internal XML-like format. The `health_agent.py` is configured to handle the standard tool-calling protocol.
- **Python Version:** The project is running on Python 3.13. Ensure all library installations are compatible (use `python -m pip`).
- **State Persistence:** The current agent implementation is stateless for simplicity. Session history is managed by the UI layer (Streamlit).
