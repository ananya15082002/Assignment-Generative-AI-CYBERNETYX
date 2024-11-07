import requests
from concurrent.futures import ThreadPoolExecutor

# Endpoint URL for querying
url = "http://127.0.0.1:8000/query"

def query_document(query_text):
    data = {"query": query_text}
    response = requests.post(url, json=data)
    return response.json()

def concurrency_test():
    # Prompt user for number of queries
    num_queries = int(input("Enter the number of queries to send concurrently: "))
    queries = [input(f"Enter query {i + 1}: ") for i in range(num_queries)]
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(query_document, queries))
    
    for i, result in enumerate(results, 1):
        print(f"Response {i}: {result}")

if __name__ == "__main__":
    concurrency_test()
