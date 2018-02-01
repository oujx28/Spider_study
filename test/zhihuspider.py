# coding:utf-8

import re
import requests
def get_xsrf(session):
    index_url = 'http://www.zhihu.com'
    index_page = session.get(index_url, headers=headers)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    _xsrf = re.findall(pattern, html)
    return _xsrf[0]


user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/49.0'
headers = {'User-Agent':user_agent}

session = requests.session()
_xsrf = get_xsrf(session)
post_url = 'http://www.zhihu.com/login/phone_num'
postdata = {
    '_xsrf': _xsrf,
    'password': 'xxxxxxxx',
    'remember_me': 'true',
    'phone_num': 'xxxxx'
}

login_page = session.post(post_url, data=postdata, headers=headers)
login_code = login_page.text
print(login_page.status_code)
print(login_code)
