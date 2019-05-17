import re
from bs4 import BeautifulSoup
from common import load_page

class page_bot(object):
    def __init__(self, url: str, params: dict = None):
        self.url = url
        self.params = params
        self.soup = None

    def get_soup(self):
        self.soup = load_page(self.url, self.params)

class naver_comic(page_bot):
    def __init__(self, url, params = None):
        super(naver_comic, self).__init__(url, params)

    def read_page(self):
        self.get_soup()
        
        img_tags = self.soup.select('div.view_area > div.wt_viewer > img')
        for img_tag in img_tags:
            if img_tag.attrs['alt'] == 'comic content':
                print(img_tag.attrs['src'])

page = naver_comic('comic.naver.com/webtoon/detail.nhn', {'titleId':675554, 'no':795, 'weekday':'mon'})
page.read_page()
