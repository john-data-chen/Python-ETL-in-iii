# coding=utf-8
__author__ = 'john.chen'

import requests
from bs4 import BeautifulSoup
import os

if not os.path.exists("ptt_movie"):
    os.mkdir("ptt_movie")

for i in range(2399, 2403):
    res = requests.get("https://www.ptt.cc/bbs/movie/index%d.html"%i, verify = False)
    soup = BeautifulSoup(res.text)
    tr = soup.select(".r-ent")
    for rec in tr:
        title_list = open("ptt_movie/title_list.txt", "a")
        title_list.write(rec.select(".title")[0].text.encode("utf-8").strip() + "\n")
        title_list.close()
print "清單產生完畢"