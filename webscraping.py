import requests
from bs4 import BeautifulSoup

url = "https://g1.globo.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("Notícias capturadas do G1:")
for i, noticia in enumerate(soup.find_all("a", class_="feed-post-link")[:5], start=1):
    print(f"{i}. {noticia.text.strip()}")
    
    
# As bibliotecas usadas:
# 1. requests: A biblioteca requests serve para fazer requisições HTTP
# 2. BeautifulSoup: serve para analisar e navegar pelo código HTML que o requests trouxe.


