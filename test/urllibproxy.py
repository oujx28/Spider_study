# coding:utf-8

from urllib import request

proxy = request.ProxyHandler({'http':'127.0.0.1:8087'})
opener = request.build_opener(proxy)
response = opener.open('http://httpbin.org/get')

print(response.read())