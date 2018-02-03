# coding:utf-8

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from cnblogSpider.items import CnblogspiderItem


class CnblogsSpider(CrawlSpider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = [
        "http://www.cnblogs.com/qiyeboy/default.html?page=1"
    ]

    rules = (
        Rule(LinkExtractor(allow=("/qiyeboy/default.html\?page=\d{1,}",)),
             follow=True, callback='parse_item'),
    )

    def parse_item(self, response):
        print(response)
        papers = response.xpath(".//div[@class='day']")

        #from scrapy.shell import inspect_response
        #inspect_response(response, self)

        for paper in papers:
            url = paper.xpath(".//div[@class='postTitle']/a/@href").extract_first()
            title = paper.xpath(".//div[@class='postTitle']/a/text()").extract_first()
            time = paper.xpath(".//div[@class='dayTitle']/a/text()").extract_first()
            content = paper.xpath(".//div[@class='postCon']/div/text()").extract_first()
            item = CnblogspiderItem(url=url, title=title, time=time, content=content)
            request = scrapy.Request(url=url, callback=self.parse_body)
            request.meta['item'] = item
            yield request

        #next_page = Selector(response).re(u'<a href="(\S*)">下一页</a>')
        #if next_page:
        #    yield scrapy.Request(url=next_page[0], callback=self.parse)

    def parse_body(self, response):
        item = response.meta['item']
        body = response.xpath(".//*[@class='postBody']")
        item['cimage_urls'] = body.xpath('.//img/@src').extract()
        yield item