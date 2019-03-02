#utf-8
from scrapy import Request
from scrapy.spider import Spider
from JobWeb.items import NeiTui
from JobWeb.Requesthead import NeiTuiHeaders

class NeiTuiSpider(Spider):
    name = 'NeiTui'
    def start_requests(self):
        url = 'http://www.neitui.me/?name=job&handle=lists'
        yield Request(url = url, headers = NeiTuiHeaders)
    def parse(self, response):
        item = NeiTui()
        NEITUI = response.xpath('.//div[@class = "media"]')
        for neitui in NEITUI:
            item['NeiTuiTitle'] = neitui.xpath('.//div[@class = "mt5 clearfix"]/a/text()').extract()[0]
            item['NeiTuiCompany'] = neitui.xpath('.//div[@class = "grey mt5"]/span/a/text()').extract()[0]
            yield item

        next_Link = response.xpath('.//div[@class = "text-center"]/nav/ul/li/a[@aria-label = "Next"]/@href').extract()
        if next_Link:
            next_Link = 'http://www.neitui.me/'+next_Link[0]
            yield Request(next_Link,headers=NeiTuiHeaders)