# coding:utf-8

from dataoutput import DataOutput
from htmldownloader import HtmlDownLoader
from htmlparse import HtmlParser
from urlmanager import UrlManager

class SpiderManager(object):
    def __init__(self):
        self.urlmanager = UrlManager()
        self.downloader = HtmlDownLoader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        self.urlmanager.add_new_url(root_url)

        while (self.urlmanager.has_new_url() and self.urlmanager.old_url_size() < 100):
            try:
                new_url = self.urlmanager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls, data = self.parser.parser(new_url, html)
                self.urlmanager.add_new_urls(new_urls)
                self.output.store_data(data)
                print('Has crawl %s links' % self.urlmanager.old_url_size())
            except Exception as e:
                print('crawl failed')
                print(e)
        self.output.output_html()

if __name__ == '__main__':
    spider_manager = SpiderManager()
    spider_manager.crawl('https://baike.baidu.com/item/网络爬虫')

