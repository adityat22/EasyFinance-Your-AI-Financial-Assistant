# EasyFinance

Generative AI-based financial planning assistant.

## Setup

1.  Create virtual environment: `python -m venv venv`
2.  Activate: `.\venv\Scripts\activate`
3.  Install dependencies: `pip install -r requirements.txt`

## Run

`uvicorn app.main:app --reload`

## Features

*   **Conversational AI**: Powered by OpenAI GPT-3.5 (Requires API Key).
*   **Simulation Mode**: Works without an API Key! Can fetch stock prices and search the PDF report using keyword matching.
*   **Budgeting & Finance**: Real-time stock data via Yahoo Finance.
*   **RAG**: Retrieval-Augmented Generation for project documentation.
