#utf-8
from scrapy import Request
from scrapy.spider import Spider
from JobWeb.items import JobwebItem
from JobWeb.Requesthead import Bossheaders
class BossSpider(Spider):
    name = 'Boss'
    def start_requests(self):
        url = 'https://www.zhipin.com/c100010000/?page=1&ka=page-1'
        yield Request(url =url,headers= Bossheaders)
    def parse(self,response):
        item = JobwebItem()
        Boss = response.xpath('//div[@class = "job-list"]/ul/li')
        for boss in Boss:
            item['jobTitle'] = boss.xpath('.//div[@class = "job-title"]/text()').extract()[0]
            item['Salary'] = boss.xpath('.//div[@class = "info-primary"]/h3/a/span/text()').extract()[0]
            item['jobSite'] = boss.xpath('.//div[@class = "info-primary"]/p/text()[1]').extract()[0]
            item['jobExperience'] = boss.xpath('.//div[@class = "info-primary"]/p/text()[2]').extract()[0]
            item['jobFinancing'] = boss.xpath('.//div[@class = "info-primary"]/p/text()[3]').extract()[0]
            item['jobCompany'] = boss.xpath('.//div[@class = "company-text"]/h3/a/text()').extract()[0]
            yield  item

        next_link = response.xpath('.//div[@class = "page"]/a[@class = "next"]/@href').extract()
        if next_link:
            next_link = 'https://www.zhipin.com/c100010000/' + next_link[0]
            yield Request(next_link, headers=Bossheaders)