# coding:utf-8

import urllib
from urllib import request
from http import cookiejar

#url = 'http://httpbin.org/get'
#url = 'http://www.baidu.com'
url = 'http://www.zhihu.com'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

cookie = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)

req = request.Request(url=url, headers=headers)

response = opener.open(req)

#print(response.read().decode('utf-8'))

for item in cookie:
    print('Name = %s Value = %s' % (item.name, item.value))