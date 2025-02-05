import requests

def query_ollama(prompt):
    """Function to send a request to the Ollama model."""
    ollama_url = "http://localhost:11434/completion"  # Ensure this matches your Ollama URL and port
    data = {
        "prompt": prompt,
        "max_tokens": 150,  # Adjust max tokens as needed
        "temperature": 0.7,  # Adjust for creativity level
        "top_p": 1,
    }
    try:
        response = requests.post(ollama_url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()['completion']
    except requests.exceptions.RequestException as e:
        print(f"Error querying Ollama: {e}")
        return None

def retrieve_content(topic):
    """Function to simulate content retrieval based on a topic."""
    # Replace this with actual content retrieval logic, e.g., from a database or API
    return f"Retrieved information about {topic} from the database."

def main():
    topic = input("What topic would you like to know more about? ")
    retrieved_content = retrieve_content(topic)
    print("Retrieved Content:")
    print(retrieved_content)

    # Now use the retrieved content as context for the Ollama model
    prompt = f"{retrieved_content}\n\nBased on this information, can you provide more insights about {topic}?"
    
    fun_response = query_ollama(prompt)
    if fun_response:
        print("\nOllama Response:")
        print(fun_response)

if __name__ == "__main__":
    main()
