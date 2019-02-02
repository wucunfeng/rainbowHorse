#utf-8
from scrapy import Request
from scrapy.spider import Spider
from JobWeb.items import LaGouItem
from JobWeb.Requesthead import LaGouheaders
class LaGouSpider(Spider):
    name = 'LaGou'
    def start_requests(self):
        url = 'https://www.lagou.com/zhaopin/'
        yield Request(url=url,headers=LaGouheaders)
    def parse(self, response):
        item = LaGouItem()
        LaGou = response.xpath('//div[@class = "list_item_top"]')
        for lagou in LaGou:
            item['LaGouTitle'] = lagou.xpath('.//div[@class = "p_top"]//h3/text()').extract()[0]
            item['LaGouSalary'] = lagou.xpath('.//div[@class = "li_b_l"]/span[@class = "money"]/text()').extract()[0]
            item['LaGouSite'] = lagou.xpath('.//div[@class = "p_top"]//span[@class = "add"]/em/text()').extract()[0]
            item['LaGouCompany'] = lagou.xpath('.//div[@class = "company_name"]/a/text()').extract()[0]
            yield item

    #翻页暂时还没写出来先这样用着吧- -