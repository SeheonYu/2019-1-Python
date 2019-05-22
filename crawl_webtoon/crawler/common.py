import requests
from bs4 import BeautifulSoup

def refine_url(url):
    if 'http://' not in url and 'https://' not in url:
        url = 'https://' + url
    
    return url

def load_page(url, params = None, make_soup = True):
    url = refine_url(url)

    if params:
        html = requests.get(url, params)
    else:
        html - requests.get(url)

    if make_soup:
        soup = BeautifulSoup(html.text, 'lxml')
        return soup
    else:
        return html