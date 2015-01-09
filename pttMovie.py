#! coding=UTF-8
__author__ = 'john.chen'

import requests
from bs4 import BeautifulSoup
import os

if not os.path.exists('ppt_movie'):
    os.mkdir('ppt_movie')
for i in range(2420, 2400, -1):
    res = requests.get("https://www.ptt.cc/bbs/movie/index%d.html"%i, verify = False)
    soup = BeautifulSoup(res.text)
    tr = soup.select(".r-ent")
    for rec in tr:
        if "好雷" in rec.select('.title')[0].text.encode("utf-8").strip():
            good_list = open("ppt_movie/good_list.txt", "a")
            good_list.write(rec.select(".title")[0].text.encode("utf-8").strip() + "\n")
            good_list.close()
        if "普雷" in rec.select('.title')[0].text.encode("utf-8").strip():
            normal_list = open("ppt_movie/normal_list.txt", "a")
            normal_list.write(rec.select(".title")[0].text.encode("utf-8").strip() + "\n")
            normal_list.close()
        if "負雷" in rec.select('.title')[0].text.encode("utf-8").strip():
            bad_list = open("ppt_movie/bad_list.txt", "a")
            bad_list.write(rec.select(".title")[0].text.encode("utf-8").strip() + "\n")
            bad_list.close()
print "所有清單已產生完畢"