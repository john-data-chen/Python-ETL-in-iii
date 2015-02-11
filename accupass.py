# encode=utf-8

import requests
from bs4 import BeautifulSoup

res = requests.get("http://www.accupass.com/search/r/1/5/0/0/1/0", verify = False)
soup = BeautifulSoup(res.text)

for event in soup.select(".APCSS_linkBox-event"):
    print ' '.join(event.text.split())