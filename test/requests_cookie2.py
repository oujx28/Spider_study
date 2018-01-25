# coding:utf-8

import requests

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
headers = {'User-Agent':user_agent}
cookies = dict(name='Cookies99', age='88')
r = requests.get('http://httpbin.org/get', headers=headers, cookies=cookies)
print(r.text)