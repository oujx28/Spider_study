# -*- coding:utf-8 -*-

import random
import time, threading

class myThread(threading.Thread):
    def __init__(self, name, urls):
        threading.Thread.__init__(self, name=name)
        self.urls = urls

    def run(self):
        print('Current %s is running...' % threading.current_thread().name)
        for url in self.urls:
            print('%s --->> %s' % (threading.current_thread().name, url))
            time.sleep(random.random())
        print('%s ended.' % threading.current_thread().name)

print('%s is running...' % threading.current_thread().name)
t1 = myThread(name='Thread_1', urls=['url_1', 'url_2', 'url_3'])
t2 = myThread(name='Thread_2', urls=['url_4', 'url_5', 'url_6'])

t1.start()
t2.start()
t1.join()
t2.join()
print('%s ended.' % threading.current_thread().name)
