#! coding=UTF-8
__author__ = 'john.chen'

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.google.com/news?cf=all&ned=tw&hl=zh-TW', verify = False)
soup = BeautifulSoup(res.text)

# 抓出.topic裡面的title、
for title in soup.select(".titletext"):
    print title.text.strip()
