# 🧠 Doc-Weaver

An intelligent AI document generation agent that transforms natural
language requests into professional Microsoft Word documents through
autonomous planning, reflection, and LLM-powered content generation.
Built with **FastAPI** and **Groq (Llama 3.3 70B)**.

------------------------------------------------------------------------

## ✨ Features

-   🤖 **Autonomous Planning** -- Analyzes user requests and generates a
    structured execution plan.
-   🧠 **Assumption Generation** -- Identifies missing information and
    makes reasonable assumptions.
-   📝 **AI-Powered Content Generation** -- Produces detailed,
    well-structured business documents using Groq LLMs.
-   🔍 **Reflection & Self-Review** -- Reviews and improves generated
    content before exporting.
-   📄 **Microsoft Word Export** -- Automatically generates
    professionally formatted `.docx` documents.
-   ⚡ **REST API** -- Built with FastAPI for easy integration with
    other applications.
-   🧩 **Modular Architecture** -- Separate planner, executor, tools,
    reflection, and document generation components.

------------------------------------------------------------------------

# 🚀 Development Setup

## 1️⃣ Prerequisites

-   Python **3.10+**
-   A free **Groq API Key**
-   Git

------------------------------------------------------------------------

## 2️⃣ Installation

``` bash
git clone https://github.com/<your-username>/doc-weaver.git

cd doc-weaver

pip install -r requirements.txt
```

------------------------------------------------------------------------

## 3️⃣ Setup API Key (Important!)

Create a `.env` file:

``` env
GROQ_API_KEY=gsk_your_api_key_here
```

> **Note:** The `.env` file is ignored by Git to keep your API key
> private.

------------------------------------------------------------------------

## 4️⃣ Run the Application

``` bash
uvicorn app:app --reload
```

Open:

``` text
http://127.0.0.1:8000/docs
```

------------------------------------------------------------------------

# 📦 API Usage

## Endpoint

``` http
POST /agent
```

### Example Request

``` json
{
  "request": "Create a project proposal for an AI chatbot for a hospital."
}
```

### Example Response

``` json
{
  "status": "success",
  "goal": "Create Business Proposal",
  "assumptions": [
    "Timeline assumed to be 6 months.",
    "Existing CRM system is available."
  ],
  "plan": [
    "Analyze Request",
    "Identify Assumptions",
    "Create Proposal Outline",
    "Generate Proposal",
    "Review Proposal",
    "Generate DOCX"
  ],
  "document": "generated_docs/document_xxxxx.docx",
  "message": "Document generated successfully."
}
```

------------------------------------------------------------------------

# 🏗️ Project Structure

``` text
doc-weaver/

├── agent/
│   ├── planner.py
│   ├── executor.py
│   ├── reflector.py
│   └── tools.py
│
├── services/
│   ├── llm.py
│   └── document_generator.py
│
├── app.py
├── schemas.py
├── requirements.txt
├── README.md
└── .gitignore
```

------------------------------------------------------------------------

# ⚙️ Agent Workflow

``` text
User Request
      │
      ▼
Planner Agent
      │
      ▼
Goal + Assumptions + Task List
      │
      ▼
Executor
      │
      ├── Generate Outline
      ├── Generate Proposal
      ├── Review Document
      └── Export DOCX
      │
      ▼
Professional Word Document
```

------------------------------------------------------------------------

# 🛠️ Tech Stack

-   FastAPI
-   Python
-   Groq (Llama 3.3 70B)
-   python-docx
-   Pydantic
-   python-dotenv
-   Uvicorn

------------------------------------------------------------------------

# 🔮 Future Improvements

-   Multi-agent architecture
-   Memory-enabled planning
-   Retrieval-Augmented Generation (RAG)
-   PDF export
-   Web search integration
-   Custom document templates

------------------------------------------------------------------------

# 📜 License

This project is intended for educational and demonstration purposes.
