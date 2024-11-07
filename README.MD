# Assignment-Generative-AI-CYBERNETYX

## Project Overview
This project is a lightweight FastAPI server implementing Retrieval-Augmented Generation (RAG) using ChromaDB for persistent storage of document embeddings. It supports uploading documents (PDF, DOC, DOCX, TXT), embedding them, and querying based on content similarity.

## Directory Structure
Assignment-Generative-AI-CYBERNETYX/ ├── main.py # FastAPI server code ├── requirements.txt # Dependencies ├── README.md # Documentation ├── tests/ │ ├── ingest_test.py # Script to test ingestion endpoint │ ├── query_test.py # Script to test query endpoint │ └── concurrency_test.py # Script to test concurrent requests └── docs/ └── example_files/ # Example documents for testing ├── ai.docx ├── genai.pdf └── ml.txt
