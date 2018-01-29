# coding:utf-8

import json
from bs4 import BeautifulSoup
import requests

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
headers = {'User-Agent':user_agent}
res = requests.get('http://seputu.com/', headers=headers)
soup = BeautifulSoup(res.content, 'lxml')
content = []

for mulu in soup.findAll(class_='mulu'):
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string
        list = []
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            list.append({'href':href, 'box_title':box_title})
        content.append({'title':h2_title, 'content':list})

with open('test.json', 'w') as fp:
    json.dump(content, fp=fp, indent=4)