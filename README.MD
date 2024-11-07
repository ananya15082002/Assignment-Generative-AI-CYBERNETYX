# Assignment-Generative-AI-CYBERNETYX

## Problem Statement
With the growing need for efficient document storage and retrieval systems, particularly in fields where documents contain valuable information (e.g., research, legal, healthcare), there’s a demand for systems that can easily store documents, generate content-based embeddings, and allow for powerful search capabilities.

The challenge is to create a system that can:
1. **Ingest various document types (PDF, DOCX, TXT)**
2. **Generate embeddings for document content**
3. **Store these embeddings in a persistent database**
4. **Provide fast and relevant search results based on content similarity**

## Solution
Our solution is a lightweight FastAPI server implementing **Retrieval-Augmented Generation (RAG)** using **ChromaDB** for persistent storage of document embeddings. It leverages the **all-MiniLM-L6-v2** model from Hugging Face's `sentence-transformers` to generate text embeddings. With non-blocking API endpoints, this setup supports efficient document ingestion and query-based retrieval.

This project:
1. **Creates a server using FastAPI** to handle requests.
2. **Ingests documents** by uploading files, extracting their text, generating embeddings, and storing them in ChromaDB.
3. **Enables querying of documents** by using content similarity with generated embeddings.

## Project Structure
The following structure organizes the main server code, testing scripts, and sample documents for easy use and testing:

Assignment-Generative-AI-CYBERNETYX/ ├── main.py # FastAPI server code ├── requirements.txt # Dependencies ├── README.md # Documentation ├── tests/ │ ├── ingest_test.py # Script to test ingestion endpoint │ ├── query_test.py # Script to test query endpoint │ └── concurrency_test.py # Script to test concurrent requests └── docs/ └── example_files/ # Example documents for testing ├── ai.docx ├── genai.pdf └── ml.txt
