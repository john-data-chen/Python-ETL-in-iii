# coding=utf-8
__author__ = 'john.chen'

import requests
from bs4 import BeautifulSoup

# 連抓2014年12月至10月的榜單
for i in range(12, 9, -1):
    # 模擬瀏覽器
    header = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    res = requests.get("http://www.books.com.tw/web/sys_monthtopb/books/?year=2014&month=%d"%i, verify = False)
    soup = BeautifulSoup(res.text)

    for stitle in soup.select(".alpha"):
        print stitle.text.strip()