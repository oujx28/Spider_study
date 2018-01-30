# coding:utf-8

from multiprocessing.managers import BaseManager
from multiprocessing import Process, freeze_support, Queue
from urlmanager import UrlManager
from dataoutput import DataOutput
import time

class TaskMananger():

    def start_manager(self, url_q, result_q):
        BaseManager.register('get_task_queue', callable=lambda:url_q)
        BaseManager.register('get_result_queue', callable=lambda:result_q)

        manager = BaseManager(address=('', 8001), authkey='baike'.encode('utf-8'))
        return manager

    def url_manager_proc(self, url_q, conn_q, root_url):
        url_manager = UrlManager()
        url_manager.add_new_url(root_url)
        while True:
            if url_manager.has_new_url():
                new_url = url_manager.get_new_url()
                url_q.put(new_url)
                print('old_url=', url_manager.old_url_size())
                if url_manager.old_url_size() > 2000:
                    url_q.put('end')
                    print('Manager notify ending!')
                    url_manager.save_progress('new_urls.txt', url_manager.new_urls)
                    url_manager.save_progress('old_urls.txt', url_manager.old_urls)
                    return
            try:
                if not conn_q.empty():
                    urls = conn_q.get()
                    url_manager.add_new_urls(urls)
            except BaseException as e:
                time.sleep(0.1)

    def result_solve_proc(self, result_q, conn_q, store_q):
        while True:
            try:
                if not result_q.empty():
                    content = result_q.get(True)
                    if content['new_urls'] == 'end':
                        print('result parse process get the ending notify!')
                        store_q.put('end')
                        return
                    conn_q.put(content['new_urls'])
                    store_q.put(content['data'])
                else:
                    time.sleep(0.1)
            except BaseException as e:
                time.sleep(0.1)


    def store_proc(self, store_q):
        output = DataOutput()
        while True:
            if not store_q.empty():
                data = store_q.get()
                if data == 'end':
                    print('Store process get the ending notify')
                    return
                output.store_data(data)
            else:
                time.sleep(0.1)

if __name__ == '__main__':
    freeze_support()
    url_q = Queue()
    result_q = Queue()
    store_q = Queue()
    conn_q = Queue()
    task = TaskMananger()
    mananger = task.start_manager(url_q, result_q)
    url_manager_proc = Process(
        target=task.url_manager_proc,
        args=(url_q, conn_q, 'https://baike.baidu.com/item/网络爬虫',))
    result_solve_proc = Process(
        target=task.result_solve_proc,
        args=(result_q, conn_q, store_q,))
    store_proc = Process(
        target=task.store_proc, args=(store_q,)
    )

    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()
    mananger.get_server().serve_forever()