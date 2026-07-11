import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

url = "https://trinetra-bhojanalaya.github.io/"

response = requests.get(url, headers=headers)

print(response.status_code)

soup = BeautifulSoup(response.content, "html.parser")

print(soup.title.text)

links = soup.find_all("a")
for link in links:
    print(link.get("href"))

#CSS Selectors
# print(soup.select(".navbar"))
