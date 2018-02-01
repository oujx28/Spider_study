# coding:utf-8

import requests

class SpiderDownloader(object):
    def download(self, url):
        if url is None:
            return None
        user_agent = 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo y31 Build/LMY48Z)'
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers = headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return  r.text
        return None