# coding:utf-8

import time
from downloader import HtmlDownloader
from dataoutput import DataOutput
from htmlparser import HtmlParser

class SpiderManager(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        content = self.downloader.download(root_url)
        #with open("content.html", 'wb') as f:
        #    f.write(content.encode('utf-8'))
        urls = self.parser.parser_url(root_url, content)
        print(urls)
        for url in urls:
            try:
                t = time.strftime("%Y%m%d%H%M%S3282", time.localtime())
                rank_url = 'http://service.library.mtime.com/Movie.api' \
                    '?Ajax_CallBack=true' \
                    '&Ajax_CallBackType=Mtime.Library.Services' \
                    '&Ajax_CallBackMethod=GetMovieOverviewRating' \
                    '&Ajax_CrossDomain=1' \
                    '&Ajax_RequestUrl=%s' \
                    '&t=%s' \
                    '&Ajax_CallBackArgument0=%s' % (url[0], t, url[1])
                rank_content = self.downloader.download(rank_url)
                data = self.parser.parser_json(rank_url, rank_content)
                self.output.store_data(data)
            except Exception as e:
                print('Crawl Failed!!!')
        self.output.output_end()
        print('Crawl Finish!')


if __name__ == '__main__':
    spider = SpiderManager()
    spider.crawl('http://www.mtime.com/')