# coding:utf-8

from lxml import etree
import requests

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
headers = {'User-Agent':user_agent}

response = requests.get('http://seputu.com/', headers=headers)
html = etree.HTML(response.text)

div_mulus = html.xpath('.//*[@class="mulu"]')

for div_mulu in div_mulus:
    div_h2 = div_mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
    if len(div_h2) > 0:
        h2_title = div_h2[0]
        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            href = a.xpath('./@href')[0]
            box_title = a.xpath('./@title')[0]
            print(box_title, href)