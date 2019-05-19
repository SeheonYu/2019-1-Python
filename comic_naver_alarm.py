import requests
import time
from bs4 import BeautifulSoup

## DEF Func ##

def get_nextday_soup(wday: int):
    week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    param_week = {'week' : week[(wday + 1) % 7]}
    req = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn", params=param_week)
    soup = BeautifulSoup(req.text, 'html.parser')
    return soup

def get_title_list(soup: BeautifulSoup):
    img_list = soup.select_one('ul.img_list')
    thumb_list = img_list.select('li > dl > dt > a')
    dict_list = {}

    for i in thumb_list: # <a href="/webtoon/list.nhn?titleId=183559&amp;weekday=mon" title="신의 탑">신의 탑</a>
        href = i.get('href') # /webtoon/list.nhn?titleId=183559&weekday=mon
        href = href.split('?')[1] # titleId=183559&weekday=mon
        href = href.split('&')[0] # titleId=183559
        title_id = int(href.split('=')[1]) # 183559
        title = i.get('title') # 신의 탑

        dict_list[title_id] = title # {title : titleId}
    
    return dict_list

def is_uploaded(title_id: int):
    req = requests.get("https://comic.naver.com/webtoon/list.nhn", params={'titleId':title_id})
    soup = BeautifulSoup(req.text, 'html.parser')

    last_td_num = soup.select_one('td.num').text

    if int(last_td_num.split('.')[2]) == time.localtime().tm_mday:
        return True
    else:
        return False

## MAIN ##

soup = get_nextday_soup(time.localtime().tm_wday)
id_title_list = get_title_list(soup)

queue = []
next_queue = []
for title_id in id_title_list.keys(): # initialize next_queue
    next_queue.append(title_id) 

while True:
    if len(next_queue) == 0:
        break

    queue = next_queue # initialize queue
    next_queue = []

    for title_id in queue:
        if is_uploaded(title_id):
            print('업로드됨:', '<' + id_title_list[title_id] + '>')
        else:
            next_queue.append(title_id)