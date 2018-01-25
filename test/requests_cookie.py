# coding:utf-8

import requests

url = 'http://www.baidu.com'
#url = 'http://httpbin.org'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
headers = {'User-Agent': user_agent}

r = requests.get(url=url, headers=headers)
for key in r.cookies.keys():
    print(key + ':' + r.cookies.get(key))