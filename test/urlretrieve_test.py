# coding:utf-8

from urllib import request
from lxml import etree
import requests

def Schedule(blocknum, blocksize, totalsize):
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100

    print('Current progress: %d' % per)

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
headers = {'User-Agent':user_agent}

r = requests.get('http://www.ivsky.com/tupian/ziranfengguang/', headers=headers)

html = etree.HTML(r.text)

img_urls = html.xpath('.//img/@src')

for index, img_url in enumerate(img_urls):
    request.urlretrieve(img_url, 'img'+str(index)+'.jpg', Schedule)
