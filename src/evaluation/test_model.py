import requests
import json

def ask_question(query):
    url = "http://127.0.0.1:8001/api/v1/chat"
    headers = {"Content-Type": "application/json"}
    data = {"query": query}
    
    print(f"Asking: {query}")
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            print("\nModel Response:")
            print(result["response"])
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    ask_question("Explain the concept of compound interest in simple terms.")
