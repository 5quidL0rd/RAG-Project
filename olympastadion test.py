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

# Scrape Wikipedia content
url = "https://en.wikipedia.org/wiki/Olympiastadion_(Berlin)"
article_content = get_wikipedia_content(url)

# Create the kid-friendly prompt
prompt = create_kid_friendly_prompt(article_content)

# Example function to use with Ollama (adjust this depending on your setup)
def query_ollama(prompt):
    # Assuming Ollama has an endpoint for sending queries
    response = requests.post(
        "http://localhost:11400/completion",
        json={"prompt": prompt, "model": "your-ollama-model-name"}
    )
    return response.json().get("text")

# Get the entertaining response
fun_response = query_ollama(prompt)

# Print the AI's response
print(fun_response)

