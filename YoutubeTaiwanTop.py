# coding = utf-8
__author__ = 'kratos.chen'

import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.youtube.com/channel/UCBcIWZhWqUwknlxikVHQoyA", verify = False)
soup = BeautifulSoup(res.text)

yt = "yt-lockup-title"
for yt in soup.select(".yt-uix-tdl"):
    print yt.text.strip()
