# EasyFinance – Your AI-Powered Financial Assistant

A **Retrieval-Augmented Generation (RAG)** application designed to act as your personal financial advisor. The system combines **semantic vector search** with **Google’s Gemini LLM** to deliver context-aware, accurate, and explainable financial advice based on your documents and queries.

This project is built with a production-oriented mindset, focusing on clean architecture, comprehensive evaluation, and user-friendly interaction.

**[🚀 View Live Application](https://adityat22-easyfinance-your-ai-financi-srcuistreamlit-app-7rxdva.streamlit.app/)**

---

## 🚀 Key Features

*   **Intelligent Semantic Search**
    Utilizes **SentenceTransformers (all-MiniLM-L6-v2)** to comprehend user intent beyond elementary keyword matching, ensuring high-fidelity retrieval from uploaded financial documents.

*   **AI-Powered Recommendations**
    Integrates **Google Gemini 2.5 Flash** to generate natural-language financial advice, explaining precisely why specific strategies are recommended for your situation.

*   **Robust Data Pipeline**
    *   Supports **PDF** document ingestion for RAG.
    *   Automated text chunking and embedding generation.
    *   Efficient vector storage using **FAISS**.

*   **Interactive UI**
    *   **Streamlit-based Interface:** Clean, responsive, and easy-to-use chat interface.
    *   **Real-time Processing:** Instant feedback on document uploads and query responses.

*   **Resilient Design**
    Implements a fallback mechanism that ensures the system remains responsive even when specific components are under load.

---

## 🧠 System Architecture

1.  **Ingestion Layer**
    Ingests and processes PDF documents, splitting text into manageable chunks for embedding.

2.  **Embedding & Vector Store**
    Transforms text chunks into dense vectors using SentenceTransformers, persisting them in a **FAISS** index for high-performance similarity search.

3.  **RAG Engine**
    Retrieves the most semantically relevant document sections and augments the context window before invoking the Gemini LLM for final response synthesis.

4.  **User Interface**
    A Streamlit application that orchestrates the user interaction, document upload, and chat history management.

---

## 📁 Project Structure

```
EasyFinance/
├── .venv/                  # Virtual environment
├── data/                   # Data storage
├── src/                    # Source code
│   ├── ui/                 # Streamlit UI logic
│   │   └── streamlit_app.py
│   ├── rag/                # Core RAG engine (if separated)
│   └── ...
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API keys)
└── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/adityat22/EasyFinance-Your-AI-Financial-Assistant.git
cd EasyFinance-Your-AI-Financial-Assistant
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv .venv
```

**Windows**

```bash
.\.venv\Scripts\Activate.ps1
```

**Mac / Linux**

```bash
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Usage

### 🔹 Run the Application

To start the Streamlit app:

```bash
streamlit run src/ui/streamlit_app.py
```

This will launch the application in your default web browser.

---

## 🛠 Tech Stack

* **Language:** Python 3.13
* **Orchestration:** LangChain
* **Vector Database:** FAISS
* **LLM:** Google Gemini 2.5 Flash
* **Embeddings:** SentenceTransformers (HuggingFace)
* **Frontend:** Streamlit

---

## 📌 Use Cases

* Personal financial planning and advice
* Analyzing financial documents (e.g., reports, statements)
* Educational tool for learning about finance
* Quick retrieval of specific financial information from large documents

