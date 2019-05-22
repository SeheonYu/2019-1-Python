from bs4 import BeautifulSoup
from selenium import webdriver

import time

driver = webdriver.Chrome('Selenium\chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('tpgjsdl2')
driver.find_element_by_name('pw').send_keys('010541ysh')

# 자동입력 방지문자 입력
time.sleep(60)

# Naver 페이 들어가기
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip())
