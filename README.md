# 🩺 Healthcare Monitoring AI Agent

🚀 **An AI-powered personal health assistant** designed to help users monitor health metrics, track fitness data, retrieve reliable medical information using RAG, and check medication safety.

---

## 📖 Project Description

The **Healthcare Monitoring AI Agent** acts as a **digital health assistant** that allows users to monitor and manage their health data through natural language interaction.

Instead of manually navigating multiple applications, users can simply **ask questions or log data through a conversational interface**, and the AI agent intelligently performs the required actions.

The system integrates:

* 🧠 AI agents for natural language understanding (Groq Llama 3.3)
* 💊 Medication safety and information
* 🏃 Fitness and wellness calculations (BMI, BMR)
* 🔎 Reliable medical information lookup via RAG (Local PDFs)
* 📊 Health insights and reports

---

## ✨ Key Features

* 💊 **Medication Safety**
  * Search for general drug information
  * Check for dangerous drug-to-drug interactions
  * Retrieve usage and purpose of common medications

* 🏃 **Fitness & Wellness**
  * Calculate Body Mass Index (BMI)
  * Calculate Basal Metabolic Rate (BMR)
  * Personalized health category analysis

* 🔍 **Medical Information Lookup (RAG)**
  * Search local medical knowledge base (PDFs)
  * Retrieve document-grounded answers for symptoms and conditions
  * Context-aware retrieval using ChromaDB

* 🤖 **AI Agent Interaction**
  * Conversational health queries
  * Tool-based reasoning and automated execution
  * Strict Emergency Protocol for life-threatening symptoms

* 🖥 **Interactive Dashboard**
  * Built using **Streamlit**
  * User-friendly chat interface with patient profile sidebar

---

## 🔄 System Workflow

The system follows a **tool-based AI agent architecture** where the language model interprets user requests and decides which tools to use.

### Workflow Steps

1️⃣ **User Interaction**
Users interact through the Streamlit interface, providing queries like *"What is my BMI?"* or *"Can I take Aspirin with Warfarin?"*

2️⃣ **AI Agent Processing**
The AI agent analyzes the request using a robust tool-calling loop powered by **Groq**.

3️⃣ **Tool Selection**
The agent determines which tool should handle the task:
* 💊 Medication Tool
* 🏃 Fitness Tool
* 🔎 Medical Info (RAG) Tool

4️⃣ **Data Retrieval**
The tool retrieves data from:
* 🗄 **ChromaDB** (Local Vector Store for PDF knowledge)
* 🧬 Internal Medical Logic (for BMI/Interactions)

5️⃣ **Response Generation**
The AI agent formats the result into a clear response with a medical disclaimer.

---

## 🏗 Project Architecture

```
healthcare-ai-agent
│
├── agents/          # AI agent orchestration (SimpleHealthAgent)
├── tools/           # Agent tools (medication, fitness, medical_info)
├── database/        # DB logic (reserved for future SQL expansion)
├── ui/              # Streamlit user interface
├── vectorstore/     # RAG logic (ChromaDB, Embeddings, Ingestion)
├── data/            # Source medical PDFs
│
├── main.py          # Legacy entry point
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

---

## 🧰 Technologies Used

### 🤖 AI / Agent Frameworks
* **LangChain Core** – AI agent orchestration
* **Groq API** – Llama-3.3-70b-versatile for high-speed inference
* **ChromaDB** – Vector database for medical RAG

### 🖥 Backend & Analytics
* **Python 3.13**
* **Sentence-Transformers** – BGE-M3 local embeddings
* **Pydantic** – Data validation

### 🎨 Frontend / UI
* **Streamlit**
  * Chat-based agent interface
  * Patient profile sidebar

---

## 🎯 Learning Objectives

This project demonstrates how to:
* Build **tool-using AI agents** from scratch
* Implement **RAG (Retrieval-Augmented Generation)** with local vector stores
* Handle **asynchronous tool-calling loops** with Groq
* Design **safety-first medical protocols** in AI assistants
* Build **interactive AI dashboards** with Streamlit

---

## 📦 Installation

Clone the repository:
```bash
git clone <your-repo-url>
cd healthcare-ai-agent
```

Install dependencies:
```bash
python -m pip install -r requirements.txt
```

---

## ▶ Running the Application

Start the Streamlit interface:
```bash
python -m streamlit run ui/streamlit_app.py
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```

---

## 📜 License

This project is intended for **educational and demonstration purposes** as part of the **Capabl AI Agentic AI Program**.
