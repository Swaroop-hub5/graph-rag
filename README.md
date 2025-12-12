# 🏛️ GovTech GraphRAG Engine

[!App View](Screenshot.png)

 A Knowledge Graph-based Retrieval Augmented Generation (RAG) system designed for complex policy and legal document analysis.

## 🎯 Project Overview
Standard RAG systems often struggle with **multi-hop reasoning** (e.g., "How does Clause A affect Clause B?"). In the context of **Digital Government** and **Legal Tech**, precision is non-negotiable.

This project implements **GraphRAG**—combining Vector Search (unstructured semantic understanding) with Knowledge Graphs (structured factual relationships)—to provide accurate, hallucination-resistant answers for complex regulatory queries.

## 🛠️ Tech Stack
* **Orchestration:** LlamaIndex (PropertyGraphIndex)
* **Database:** Neo4j (Graph + Vector Store)
* **LLM & Embeddings:** Google Gemini 1.5 Flash (via Generative AI SDK)
* **Frontend:** Streamlit
* **Infrastructure:** Docker & Docker Compose
* **Language:** Python 3.10+

## 🚀 Key Features
* **Hybrid Retrieval:** Combines dense vector retrieval with graph traversal to find "hidden" connections in policy documents.
* **Automated Knowledge Construction:** Uses LLMs to extract entities (e.g., *GovernmentBody*, *Regulation*) and relationships (e.g., *ENFORCES*, *EXEMPTS*) automatically.
* **Rate-Limit Aware:** Includes a robust ingestion pipeline designed to handle API quotas gracefully.
* **Dockerized Deployment:** Fully containerized setup (Database + App) for reproducible deployment.

## 📦 How to Run

### 1. Prerequisites
* Docker Desktop (installed and running)
* Google Gemini API Key

### 2. Configure Environment
Create a '.env' file in the root directory:
```ini
GOOGLE_API_KEY=your_gemini_key_here
NEO4J_URI=bolt://neo4j:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=password123