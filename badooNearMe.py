#! coding=UTF-8
__author__ = 'john.chen'

import requests
import os

if not os.path.exists('badoo'):
    os.mkdir('badoo')
res = requests.get('http://us1.badoo.com/zh-tw/search/?interests_list=&search_button=' \
                   'search_button&interests=&r=hUU1&ebid=SppNewPeopleV2&ws=1&rt=65a631')
