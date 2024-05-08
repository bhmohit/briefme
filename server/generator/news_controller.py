import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import random

load_dotenv()



def get_news():
    response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=" + os.getenv("API_KEY"))
    response = response.json()
    
    articles = response["articles"]    
    text = requests.get(articles[random.randint(0, len(articles) - 1)]["url"])
    
    soup = BeautifulSoup(text.content, 'html.parser')
    text = soup.get_text().replace("\n", "")
    return text

def summarize_news():
    return