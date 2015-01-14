#! coding=UTF-8
__author__ = 'john.chen'

import requests
from bs4 import BeautifulSoup

for i in range(1, 3): # 從第1頁抓到第3頁
    res = requests.get('http://www.mobile01.com/topiclist.php?f=180&p=%d'%1, verify = False)
    soup = BeautifulSoup(res.text)

    # 抓出.topic裡面的title
    for title in soup.select(".topic_top"):
        print title.text.strip()
    for title in soup.select(".topic_gen"):
        print title.text.strip()