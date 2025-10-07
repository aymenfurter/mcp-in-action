import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from urllib.parse import quote_plus
import re

def search_microsoft_learn(query):
    print ("Searching for: ", query)
    api_url = f"https://learn.microsoft.com/api/search?search={quote_plus(query)}&locale=en-us&facet=category&facet=products&$filter=(category%20eq%20'Documentation')&$top=5&expandScope=true&includeQuestion=false&partnerId=LearnSite"
    
    response = requests.get(api_url)
    data = response.json()
    
    links = []
    for result in data.get('results', []):
        url = result.get('url')
        if url and '/azure/' in url:
            links.append(url)
    
    return links

def url_to_markdown(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for script in soup(["script", "style", "nav", "header", "footer"]):
        script.decompose()
    main = soup.find('main')
    if main:
        markdown = md(str(main), heading_style="ATX")
        return re.sub(r'\n\s*\n\s*\n', '\n\n', markdown).strip()
    return f"Could not extract content from {url}"
