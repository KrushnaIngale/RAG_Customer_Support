# RAG-Based Customer Support Assistant (LangGraph + HITL)

## Overview

This project is a Retrieval-Augmented Generation (RAG) based Customer Support Assistant built using:

* LangChain
* LangGraph
* ChromaDB
* Groq
* Google Gemini
* Human-in-the-Loop (HITL)

The system processes a PDF knowledge base, retrieves relevant information, answers customer queries contextually, and escalates sensitive or complex cases to human support.

---

# Features

* PDF knowledge base ingestion
* Document chunking
* Embedding generation
* Chroma vector database storage
* Semantic retrieval
* LangGraph workflow routing
* Hybrid LLM system:

  * Groq for fast responses
  * Gemini for deeper reasoning
* Human escalation for risky queries
* Modular code structure

---

# Project Architecture

```text
PDF → Chunk → Embed → ChromaDB

User Query → Retrieve Context → LangGraph Router
    ├── Groq Response
    ├── Gemini Response
    └── Human Escalation
```

---

# Folder Structure

```text
rag-project/
│── data/
│   └── support_kb.pdf
│
│── src/
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── llm.py
│   ├── graph.py
│   ├── hitl.py
│   ├── rag_pipeline.py
│
│── chroma_db/
│── .env
│── main.py
│── requirements.txt
│── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repo-link>
cd rag-project
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env`

```env
GOOGLE_API_KEY=your_google_key
GROQ_API_KEY=your_groq_key
```

---

# Run Project

```bash
python main.py
```

---

# Example Queries

* What is the refund policy?
* How do I reset my password?
* Explain refund rejection after policy expiry
* Cancel my account immediately

---

# Routing Logic

## Groq

Used for:

* Short queries
* Fast responses

## Gemini

Used for:

* Complex reasoning
* Detailed explanations

## HITL

Triggered for:

* Refund disputes
* Account cancellation
* Missing context
* Sensitive issues

---

# Tech Decisions

## Why ChromaDB?

Simple local vector database, fast for prototypes.

## Why LangGraph?

Clean stateful workflow and routing logic.

## Why Hybrid Models?

Combines speed + reasoning quality.

---

# Future Enhancements

* Streamlit Web UI
* Multi-PDF support
* Feedback learning loop
* Memory-enabled conversations
* Deployment on cloud

---

# Author

Krushna
