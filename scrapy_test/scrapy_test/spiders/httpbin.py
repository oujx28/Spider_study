# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy_test.items import  ScrapyTestItem

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        jsondata = json.loads(response.body)
        item = ScrapyTestItem(user_agent=jsondata['headers']['User-Agent'])
        yield item