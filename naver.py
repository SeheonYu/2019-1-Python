import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.naver.com")
soup = BeautifulSoup(req.text, 'html.parser')

txt = soup.select('img')
for i in txt:
    print(i.select('scr'))