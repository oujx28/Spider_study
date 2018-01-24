# -*- coding:utf-8 -*-

from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool
from urllib import request

def run_task(url):
    print('Visit --> %s' % url)
    try:
        response = request.urlopen(url)
        data = response.read()
        print('%d bytes received from %s.' % (len(data), url))
    except Exception as e:
        print(e)

    return 'url:%s ---> finish' % url

if __name__ == '__main__':
    pool = Pool(2)
    urls = [
        'https://github.com/',
        'https://www.python.org/',
        'https://www.cnblogs.com/'
    ]
    results = pool.map(run_task, urls)
    print(results)