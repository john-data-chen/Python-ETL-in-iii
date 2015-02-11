# coding=utf-8
__author__ = 'john.chen'

import requests
from bs4 import BeautifulSoup

# 排行名次
index = 1
# 每頁20條，共5頁 1<=i<6
for i in range(1, 6):
    res = requests.get("https://tw.news.yahoo.com/sentiment/informative/%d.html" % i, verify=False)
    soup = BeautifulSoup(res.text)
    for txt in soup.select("#mediasentimentlisttemp .story"):
        print index,
        index += 1
        print txt.text.strip()