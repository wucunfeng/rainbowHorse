# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobwebItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    jobTitle = scrapy.Field() #岗位
    Salary = scrapy.Field() #工资
    jobSite = scrapy.Field() #上班地点
    jobExperience = scrapy.Field() #工作经历
    jobFinancing = scrapy.Field() #学历
    jobEmployees = scrapy.Field() #公司人数
    jobRelease = scrapy.Field() #发布日期
    jobCompany = scrapy.Field() #公司名称


class LaGouItem(scrapy.Item):
    LaGouTitle = scrapy.Field()  # 岗位
    LaGouSalary = scrapy.Field()  # 工资
    LaGouSite = scrapy.Field()  # 上班地点
    LaGouCompany = scrapy.Field()  # 公司名称

class NeiTui(scrapy.Item):
    NeiTuiTitle = scrapy.Field()
    NeiTuiCompany = scrapy.Field()