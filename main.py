from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List
from chromadb import Client as ChromaClient
from sentence_transformers import SentenceTransformer
import io
from pdfminer.high_level import extract_text as pdf_extract_text
from docx import Document as docx_Document
import uuid

app = FastAPI()

# Load the embedding model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Initialize ChromaDB client and collection
chroma_client = ChromaClient()
collection = chroma_client.get_or_create_collection("documents")

# Model for query request
class QueryRequest(BaseModel):
    query: str

# Helper function to extract text from files
def extract_text_from_file(file_content, file_type):
    try:
        if file_type == "text/plain":
            return file_content.decode("utf-8")
        elif file_type == "application/pdf":
            return pdf_extract_text(io.BytesIO(file_content))
        elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = docx_Document(io.BytesIO(file_content))
            return "\n".join([paragraph.text for paragraph in doc.paragraphs])
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported file type: {file_type}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Text extraction error: {e}")

# Endpoint to ingest documents
@app.post("/ingest")
async def ingest_documents(files: List[UploadFile] = File(...)):
    document_ids = []
    for file in files:
        content = await file.read()
        text = extract_text_from_file(content, file.content_type)

        # Generate embeddings for the text
        embeddings = model.encode([text])[0]
        doc_id = str(uuid.uuid4())
        collection.add(
            ids=[doc_id],
            documents=[text],
            embeddings=[embeddings],
            metadatas=[{"filename": file.filename}]
        )
        document_ids.append(doc_id)

    return {"message": "Documents ingested successfully", "document_ids": document_ids}

# Endpoint to query documents
@app.post("/query")
async def query_documents(request: QueryRequest):
    query_embedding = model.encode([request.query])[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=10)

    documents = []
    for i, doc in enumerate(results.get("documents", [])):
        document_text = doc[0]  # Extract the document text
        filename = results["metadatas"][i][0].get("filename", "Unknown")
        documents.append({
            "filename": filename,
            "text": document_text[:100]  # Provide a text preview
        })

    # Return results or a message if none are found
    if not documents:
        return {"message": "No relevant documents found."}
    
    return {"results": documents}

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Server is running"}
