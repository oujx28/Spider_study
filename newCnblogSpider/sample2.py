# coding:utf-8

import scrapy
from twisted.internet import reactor
from scrapy.crawler  import CrawlerRunner
from scrapy.utils.log import configure_logging

class MySpider1(scrapy.Spider):
    # Your first spider definition
    pass

class MySpider2(scrapy.Spider):
    # Your second spider definition
    pass

configure_logging()
runner = CrawlerRunner()
runner.crawl(MySpider1)
runner.crawl(MySpider2)
d = runner.join()
d.addBot(lambda _: reactor.stop())
reactor.run()