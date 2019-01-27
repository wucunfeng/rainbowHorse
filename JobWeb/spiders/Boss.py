from scrapy.spider import Spider

class BossSpider(Spider):
    name = 'Boss'
    URL = ['https://www.zhipin.com/job_detail/?ka=header-job']
