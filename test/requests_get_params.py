# coding:utf-8

import requests

params = {
    'Keywords': 'blog',
    'pageindex': 1,
}

r = requests.get('http://httpbin.org/get', params=params)

print(r.url)
print(r.text)
print('encoding -->', r.encoding)