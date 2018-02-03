# coding:utf-8

import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider1(scrapy.Spider):
    # Your first spider definition
    pass

class MySpider2(scrapy.Spider):
    # Your second spider definition
    pass

process = CrawlerProcess()
process.crawl(MySpider1)
process.crawl(MySpider2)
process.start()
