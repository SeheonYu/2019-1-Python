import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.daum.net")
soup = BeautifulSoup(req.text, 'html.parser')

issue = soup.find('div', {'class', 'realtime_part'})
txt = issue.find_all('li')

n = 1
for i in txt:
    print(str(n) + '위 ' + i.find('a',{'class','link_issue'}).text)
    n += 1