import re
from font_processter import FontProcesster as FP
import time
from multiprocessing import Pool
import asyncio
import aiohttp
from lxml import etree
from pymongo import MongoClient


class InternSpider(object):
    def __init__(self, keyword, pages=0):
        super().__init__()
        self.keyword = keyword
        self.pages = pages
        self.domain = 'https://www.shixiseng.com'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
        self.fp = FP()
        self.session = aiohttp.ClientSession(headers=self.headers)
        self.writer = self.open_db()

    @staticmethod
    def process_detail(details):
        pattern = re.compile(r'\xa0|\r|\n|\s')
        job_detail = re.sub(pattern, '', details)
        return job_detail

    def open_db(self):
        client = MongoClient('localhost', 27017)
        writer = client['intern'][self.keyword]
        return writer
    # -----------------------------------------------------------------------

    async def get_intern(self, p=0):
        param = '/interns?k={k}&p={p}'.format(k=self.keyword, p=p)
        url = self.domain + param
        async with self.session.get(url) as r:
            text = await r.text()
            html = etree.HTML(text)
            links = html.xpath('//div[@class="names cutom_font"]/a/@href')
            tasks = [self.intern_detail(self.domain + link) for link in links]
            await asyncio.gather(*tasks)

        while self.pages > 0:
            self.pages -= 1
            p += 1
            await asyncio.ensure_future(self.get_intern(p=p))

    async def intern_detail(self, link):
        async with self.session.get(link) as r:
            text = await r.text()
            html = etree.HTML(text)
            job_name = html.xpath('//*[@class="new_job_name"]/text()')[0]
            job_money = html.xpath('//*[@class="job_money cutom_font"]/text()')[0]
            job_position = html.xpath('//*[@class="job_position"]/text()')[0]
            job_week = html.xpath('//*[@class="job_week cutom_font"]/text()')[0]
            job_academic = html.xpath('//*[@class="job_academic"]/text()')[0]
            job_time = html.xpath('//*[@class="job_time cutom_font"]/text()')[0]
            job_detail = html.xpath('//*[@class="job_detail"]')[0].xpath('string(.)')

            job_money = self.fp.process(job_money)
            job_week = self.fp.process(job_week)
            job_time = self.fp.process(job_time)

            job_detail = self.process_detail(job_detail)

            intern = {
                'job_name': job_name,
                'job_money': job_money,
                'job_position': job_position,
                'job_week': job_week,
                'job_academic': job_academic,
                'job_time': job_time,
                'job_detail': job_detail
            }
            self.writer.insert_one(intern)

    # ---------------------------------------------


def main(keyword, pages=0):
    c = InternSpider(keyword, pages)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(c.get_intern())
    c.session.close()


if __name__ == '__main__':
    start = time.time()
    pool = Pool(processes=3)
    keywords = ['python', '区块链', '数据分析']
    for word in keywords:
        pool.apply_async(main, args=(word, ))
    pool.close()
    pool.join()

    end = time.time()
    print(end - start)