# coding:utf-8

from urllib import request
from urllib import parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
postdata = {
    'username': 'qiye',
    'password': 'qiye_pass',
}
data = parse.urlencode(postdata).encode(encoding='utf-8')
req = request.Request(url=url, headers=headers, data=data)

response = request.urlopen(req)

print(response.read().decode('utf-8'))