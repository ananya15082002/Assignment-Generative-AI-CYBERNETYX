


## Setup Instructions

### Clone Repository
```bash
git clone https://github.com/ananya15082002/Assignment-Generative-AI-CYBERNETYX.git
cd Assignment-Generative-AI-CYBERNETYX

Install Dependencies

pip install -r requirements.txt



Start the Server
uvicorn main:app --reload

C:\Users\asus\Desktop\GenAIAssignment>cd  tests

C:\Users\asus\Desktop\GenAIAssignment\tests>python ingest_test.py
Enter the number of files to upload: 3
Enter the path for file 1: C:\Users\asus\Desktop\GenAIAssignment\docs\example_files\ai.docx
Uploading C:\Users\asus\Desktop\GenAIAssignment\docs\example_files\ai.docx with MIME type: application/vnd.openxmlformats-officedocument.wordprocessingml.document
Enter the path for file 2: C:\Users\asus\Desktop\GenAIAssignment\docs\example_files\genai.pdf
Uploading C:\Users\asus\Desktop\GenAIAssignment\docs\example_files\genai.pdf with MIME type: application/pdf
Enter the path for file 3: C:\Users\asus\Desktop\GenAIAssignment\docs\example_files\ml.txt
Uploading C:\Users\asus\Desktop\GenAIAssignment\docs\example_files\ml.txt with MIME type: text/plain
Ingestion Response: {'message': 'Documents ingested successfully', 'document_ids': ['c13c6940-500a-42c6-93c8-79542ac5d2da', 'a11b7ba4-fc59-46bc-a999-859c819f1cbd', 'fd827437-1156-4d9c-81b6-f3a967979790']}

C:\Users\asus\Desktop\GenAIAssignment\tests>python query_test.py
Enter your query text: AI
Query Results:

Document 1:
Filename: ai.docx
Text Preview: Artificial Intelligence (AI) refers to the simulation of human intelligence in machines. It allows s...


C:\Users\asus\Desktop\GenAIAssignment\tests>python query_test.py
Enter your query text: intelligent
Query Results:

Document 1:
Filename: ai.docx
Text Preview: Artificial Intelligence (AI) refers to the simulation of human intelligence in machines. It allows s...


C:\Users\asus\Desktop\GenAIAssignment\tests>python concurrency_test.py
Enter the number of queries to send concurrently: 2
Enter query 1: AI
Enter query 2: intelligent
Response 1: {'results': [{'filename': 'ai.docx', 'text': 'Artificial Intelligence (AI) refers to the simulation of human intelligence in machines. It allows s'}]}
Response 2: {'results': [{'filename': 'ai.docx', 'text': 'Artificial Intelligence (AI) refers to the simulation of human intelligence in machines. It allows s'}]}

C:\Users\asus\Desktop\GenAIAssignment\tests>

