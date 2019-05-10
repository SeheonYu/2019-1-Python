import re
import requests
import math
from bs4 import BeautifulSoup

week = {'week' : 'mon'}
req = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn", params=week)
soup = BeautifulSoup(req.text, 'html.parser')

img_list = soup.find('ul', {'class':'img_list'})
thumb_list = img_list.find_all('div', {'class':'thumb'})
id_list = []

for i in thumb_list:
    href = i.find('a').get('href') # /webtoon/list.nhn?titleId=183559&weekday=mon
    href = href.split('?')[1] # titleId=183559&weekday=mon
    href = href.split('&')[0] # titleId=183559
    titleId = {href.split('=')[0] : int(href.split('=')[1])} # 183559
    title = i.find('a').get('title') # 신의 탑

    id_list.append({'titleId':titleId, 'title':title})

url = "https://comic.naver.com/webtoon/list.nhn"
for id in id_list: # search webtoon by id
    req = requests.get(url, params=id['titleId'])
    soup = BeautifulSoup(req.text, 'html.parser')

    last_td = soup.find('td', {'class':'title'})
    href = last_td.find('a').get('href')
    last_episode = str(href).split('no=')[1]
    last_episode = int(last_episode.split('&')[0])
    
    print('<' + id['title'] + '>', last_episode, "회")
    last_episode_split10 = math.ceil(last_episode / 10)

    for page in range(1, last_episode_split10 ): # search pages ( per 10 episodes )
        params = id['titleId']
        params['page'] = page
        req = requests.get(url, params=params)
        soup = BeautifulSoup(req.text, 'html.parser')

        table = soup.find('table', {'class':'viewList'})
        tr_list = table.find_all('tr', {'class' : None})
        del tr_list[0]

        for tr in tr_list: # print each title and rating
            title = tr.find('td', {'class':'title'}).find('a').text
            rating = tr.find('strong').text
            print('제목:', title + ', 별점:',rating)

