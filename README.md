# 🩺 Healthcare Monitoring AI Agent

🚀 **An AI-powered personal health assistant** designed to help users monitor medications, track fitness data, retrieve reliable medical information, and generate simple health insights.


---

## 📖 Project Description

The **Healthcare Monitoring AI Agent** acts as a **digital health assistant** that allows users to monitor and manage their health data through natural language interaction.

Instead of manually navigating multiple applications, users can simply **ask questions or log data through a conversational interface**, and the AI agent intelligently performs the required actions.

The system integrates:

* 🧠 AI agents for natural language understanding
* 💊 Medication management
* 🏃 Fitness and wellness tracking
* 🔎 Reliable medical information lookup
* 📊 Health insights and reports

This creates a **simple yet powerful health monitoring system** that demonstrates how AI agents can automate workflows in healthcare and wellness applications.

---

## ✨ Key Features

* 💊 **Medication Tracking**

  * Add medications
  * Log medicine intake
  * Check medication schedules

* 🏃 **Fitness Monitoring**

  * Track daily steps
  * Record calories burned
  * Monitor sleep duration

* 🔍 **Medical Information Lookup**

  * Search for drug information
  * Retrieve side effects
  * Access reliable health data sources

* 📊 **Health Insights**

  * Weekly fitness summaries
  * Medication adherence tracking
  * Health trend analysis

* 🤖 **AI Agent Interaction**

  * Conversational health queries
  * Tool-based reasoning
  * Automated task execution

* 🖥 **Interactive Dashboard**

  * Built using **Streamlit**
  * User-friendly health tracking interface

---

## 🔄 System Workflow

The system follows a **tool-based AI agent architecture** where the language model interprets user requests and decides which tools to use.

### Workflow Steps

1️⃣ **User Interaction**

Users interact with the system through the Streamlit interface.

Example queries:

* *"Did I take my medicine today?"*
* *"What are the side effects of Ibuprofen?"*
* *"How many steps did I walk this week?"*

---

2️⃣ **AI Agent Processing**

The AI agent analyzes the request using **LangChain / LangGraph reasoning workflows**.

---

3️⃣ **Tool Selection**

The agent determines which tool should handle the task:

* 💊 Medication Tool
* 🏃 Fitness Tracking Tool
* 🔎 Medical Information Tool

---

4️⃣ **Data Retrieval**

The tool retrieves data from:

* 🗄 MySQL Database
* 🌐 External Medical APIs

---

5️⃣ **Response Generation**

The AI agent formats the result into a clear response for the user.

---

6️⃣ **Dashboard Output**

The final result is displayed in the **Streamlit dashboard**.

---

## 🏗 Project Architecture

The project follows a **modular architecture** to keep the system maintainable and scalable.

```
healthcare-ai-agent
│
├── agents/          # AI agent orchestration logic
├── tools/           # Agent tools (medication, fitness, medical info)
├── database/        # Database connection and schema
├── models/          # Data models and validation schemas
├── services/        # Background services (reminders, analytics)
├── ui/              # Streamlit user interface
├── utils/           # Utility functions and logging
│
├── main.py          # Application entry point
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

---

## 🧰 Technologies Used

### 🤖 AI / Agent Frameworks

* **LangChain** – AI agent orchestration
* **LangGraph** – advanced agent workflows
* **Groq API** – high-performance LLM inference

---

### 🖥 Backend Technologies

* **Python**
* **Pandas** – health data processing
* **Pydantic** – data validation

---

### 🗄 Database

* **MySQL**
* Structured storage for:

  * Users
  * Medications
  * Medication logs
  * Fitness data
  * Health goals

---

### 🌐 External APIs

* **OpenFDA API** – drug information and safety data
* **MedlinePlus API** – medical knowledge and disease information
* **Nutrition APIs (optional)** – dietary data

---

### 🎨 Frontend / UI

* **Streamlit**

  * Health dashboards
  * Chat-based agent interface
  * Data visualization

---

### 🛠 Development Tools

* **Git & GitHub** – version control
* **VS Code** – development environment
* **Virtual Environment (.venv)** – dependency isolation

---

## 🎯 Learning Objectives

This project demonstrates how to:

* Build **tool-using AI agents**
* Design **AI-powered workflows**
* Integrate **external APIs with LLM agents**
* Manage **health data with structured databases**
* Build **interactive AI dashboards**

It also provides hands-on experience with **real-world AI system design**.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/healthcare-ai-agent.git
cd healthcare-ai-agent
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Application

Start the Streamlit interface:

```bash
streamlit run ui/streamlit_app.py
```

The dashboard will open in your browser.

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=health_agent_db
```

---

## 📌 Future Improvements

Potential enhancements include:

* 🧠 Predictive health analytics using ML models
* 🎤 Voice-based health queries
* 📷 Pill identification using computer vision
* 🏥 Integration with electronic health records
* 📱 Mobile-friendly interface

---

## 📜 License

This project is intended for **educational and demonstration purposes** as part of the **Capabl AI Agentic AI Program**.

---

