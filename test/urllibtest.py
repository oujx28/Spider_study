# coding: utf-8

from urllib import request

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

req = request.Request(url='http://www.zhihu.com', headers=headers)

response = request.urlopen(req)

print(response.read().decode('utf-8'))