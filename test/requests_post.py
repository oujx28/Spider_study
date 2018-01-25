
# coding:utf-8

import requests

postdata = {
    'key1':'value1'
}

r = requests.post('http://httpbin.org/post', data=postdata)

print(r.text)