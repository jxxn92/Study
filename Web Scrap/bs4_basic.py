import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print(soup.title)
print(soup.title.get_text())

print(soup.div.attrs)