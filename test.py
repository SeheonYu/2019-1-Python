import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.naver.com")
soup = BeautifulSoup(req.text, 'html.parser')

for i in range(1,20):
    text = soup.find("img",{'src':i})
    txt = text.find("span",{'class':'ah_k'})
    if txt.text == '사나':
        break

if txt.text != '사나':
        print("No Sana")
else:
        print(soup.find("li",{'data-order':i}).find("span",{'class','ah_r'}).text + "위")
        print(txt.text)