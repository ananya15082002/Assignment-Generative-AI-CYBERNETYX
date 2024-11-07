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



## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/ananya15082002/Assignment-Generative-AI-CYBERNETYX.git
cd Assignment-Generative-AI-CYBERNETYX

2. Install Dependencies
Install the necessary libraries:

bash
Copy code
pip install -r requirements.txt

3. Start the FastAPI Server
Run the server locally with:

bash
Copy code
uvicorn main:app --reload
The server should now be accessible at http://127.0.0.1:8000.


Example using ingest_test.py
Navigate to the tests folder:
bash
Copy code
cd tests
Run ingest_test.py to upload multiple documents:
bash
Copy code
python ingest_test.py
You will be prompted to enter file paths. For example:
plaintext
Copy code
Enter the number of files to upload: 3
Enter the path for file 1: C:\Users\asus\Desktop\GenAIAssignment\docs\example_files\ai.docx
Enter the path for file 2: C:\Users\asus\Desktop\GenAIAssignment\docs\example_files\genai.pdf
Enter the path for file 3: C:\Users\asus\Desktop\GenAIAssignment\docs\example_files\ml.txt
2. Query Documents
The /query endpoint allows querying documents based on content similarity by embedding the query text and finding relevant documents.

Example using curl
bash
Copy code
curl -X POST "http://127.0.0.1:8000/query" -H "Content-Type: application/json" -d "{\"query\": \"Artificial Intelligence\"}"
Example using query_test.py
Run query_test.py to query based on user input:

bash
Copy code
python query_test.py
Example interaction:

plaintext
Copy code
Enter your query text: AI
Query Results:

Document 1:
Filename: ai.docx
Text Preview: Artificial Intelligence (AI) refers to the simulation of human intelligence in machines...
3. Concurrency Test
To test how well the system handles concurrent requests, run the concurrency_test.py script:

bash
Copy code
python concurrency_test.py
Example interaction:

plaintext
Copy code
Enter the number of queries to send concurrently: 2
Enter query 1: AI
Enter query 2: intelligent
Response 1: {'results': [{'filename': 'ai.docx', 'text': 'Artificial Intelligence (AI) refers to the simulation of human intelligence...'}]}
Response 2: {'results': [{'filename': 'ai.docx', 'text': 'Artificial Intelligence (AI) refers to the simulation of human intelligence...'}]}

Conclusion
This project provides a complete solution for content-based document retrieval using a lightweight FastAPI server, ChromaDB, and sentence-transformers. It allows easy ingestion, storage, and querying of documents, making it highly useful for applications requiring content similarity search capabilities.
