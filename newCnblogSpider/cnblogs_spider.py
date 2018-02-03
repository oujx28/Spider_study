# coding:utf-8

from scrapy.crawler import CrawlerProcess
from cnblogSpider.spiders.cnblogs_spider import CnblogsSpider

if __name__ == '__main__':
    process = CrawlerProcess({
            'USER_AGENT':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })

    process.crawl(CnblogsSpider)
    process.start()