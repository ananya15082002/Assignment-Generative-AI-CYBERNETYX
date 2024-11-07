import requests

# Endpoint URL
url = "http://127.0.0.1:8000/query"

# Prompt user for query input
query_text = input("Enter your query text: ")

# Data payload as JSON
data = {"query": query_text}

# Send POST request
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 200:
    results = response.json().get("results")

    # Display results if documents are found
    if isinstance(results, list):
        print("Query Results:\n")
        for i, result in enumerate(results, 1):
            print(f"Document {i}:")
            print(f"Filename: {result['filename']}")
            print(f"Text Preview: {result['text'][:500]}...\n")  # Show a 100-char preview
    else:
        print(results)  # Print message if no documents found
else:
    print(f"Error occurred while querying: {response.status_code} {response.reason}")
