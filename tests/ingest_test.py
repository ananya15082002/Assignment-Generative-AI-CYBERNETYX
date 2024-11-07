import mimetypes

import requests

# Endpoint URL for ingestion
url = "http://127.0.0.1:8000/ingest"

def ingest_files():
    num_files = int(input("Enter the number of files to upload: "))
    files = []
    for i in range(num_files):
        file_path = input(f"Enter the path for file {i + 1}: ")
        mime_type = mimetypes.guess_type(file_path)[0]  # Guess MIME type
        print(f"Uploading {file_path} with MIME type: {mime_type}")
        try:
            files.append(("files", (file_path, open(file_path, "rb"), mime_type)))
        except FileNotFoundError:
            print(f"File {file_path} not found. Please enter a valid file path.")
            return

    # Send the request
    response = requests.post(url, files=files)

    # Close all file handles after the request completes
    for _, file_info in files:
        file_info[1].close()

    print("Ingestion Response:", response.json())

if __name__ == "__main__":
    ingest_files()
