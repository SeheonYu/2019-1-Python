from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')

web = webdriver.Chrome('selenium\chromedriver.exe',options = options)

url = 'https://www.pinterest.co.kr'
search = input('검색어를 입력해주세요: ')

web.get(url + '/search/pins/?q=' + search)

last_height = 0
SCROLL_PAUSE_TIME = 0.5
HIT_LIMIT = 10

hit = 0
scroll = 0

while hit < HIT_LIMIT:
    scroll += 1
    print(scroll)

    hit = 0
    while (last_height == web.execute_script("return document.body.scrollHeight") )&( hit < HIT_LIMIT):
        print('pause', hit)
        time.sleep(SCROLL_PAUSE_TIME)
        hit += 1

    last_height = web.execute_script("return document.body.scrollHeight")
    web.execute_script("window.scrollTo(0, document.body.scrollHeight);")

html = web.page_source
soup = BeautifulSoup(html, 'lxml')

image_list = soup.select('div.Grid__Item')

n = 1
for item in image_list:
    image = item.find('a')
    print(str(n) + ": " + url + image['href'])
    n += 1

web.quit()