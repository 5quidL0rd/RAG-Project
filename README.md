# 2-part RAG project

--------------------------------------------

# olympastadion test.py


## **What it Does**


1) Scrapes Wiki Content: retrievies text from the Wiki page about this stadium

2) Builds a kid-friendly prompt with a prompt template specifically instructing the AI to design the response for small children

3) Queries the AI: it sends this prompt to an AI endpoint (Ollama here) to get a creative narrative.


## Key Code Snippets

```bash
import requests
from bs4 import BeautifulSoup

# Function to scrape Wikipedia article content
def get_wikipedia_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text from all paragraphs
    paragraphs = soup.find_all('p')
    content = "\n".join([para.get_text() for para in paragraphs])

    return content

# Scrape Wikipedia content
url = "https://en.wikipedia.org/wiki/Olympiastadion_(Berlin)"
article_content = get_wikipedia_content(url)
```

The above shows the code that fetchs the content from wiki and extracts the paragraph text


```bash
# Fun prompt template for young kids
def create_kid_friendly_prompt(article_content):
    return f"""
You are a super fun and silly tour guide talking to young kids! 
Tell the kids a story about the Olympiastadion in Berlin using the information below.

Here’s what you should do:
1. Use fun words and jokes.
2. Explain it as if the stadium is a cool character with a personality.
3. Add something silly, like how the stadium loves cheering or thinks footballs are giant cookies!

Here’s the information about the stadium:

{article_content}

Now, turn this into a fun story for kids!
"""

# Create the kid-friendly prompt
prompt = create_kid_friendly_prompt(article_content)
```
The above demonstrates the construction of a creative prompt by embedding the wiki article content into a prompt template


```bash
# Example function to use with Ollama (adjust this depending on your setup)
def query_ollama(prompt):
    response = requests.post(
        "http://localhost:11400/completion",
        json={"prompt": prompt, "model": "your-ollama-model-name"}
    )
    return response.json().get("text")

# Get the entertaining response
fun_response = query_ollama(prompt)

# Print the AI's response
print(fun_response)
```
Here the code sents the kid-friendly message


## File 2: Generalized Content Retrival and Insight Generation

This file is much less esoteric in nature. 

What it does:
1) Retrives topic content: simulates fetching content for a topic provided by the user

2) Builds a general insight prompt

3) Queries the AI

4) Easily tailorable for whatever you want if you have an article or API key you wish it to use specifically

   1. Simulating content retrieval:

```bash
def retrieve_content(topic):
    """Function to simulate content retrieval based on a topic."""
    # Replace this with actual content retrieval logic, e.g., from a database or API
    return f"Retrieved information about {topic} from the database."
```


2. User Input and Prompt Construction:

```bash
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
```

3. Querying Ollama with Parameters

   ```bash
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
   ```

#What they have in Common

1) Both of these files aim to generate creative responses by constructing detailed prompts

2) The first file focuses on converting real-world data into a fun narrative while the second provides a more generic framework where the user supplies a topic and the program retrieves associated content for the AI to look for more insights

3) Complementary Usage: The first can be used for educational purposes wil the second is suited for interactive, information-based queries
   
