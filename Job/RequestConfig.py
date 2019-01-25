import requests
from bs4 import BeautifulSoup
import time
bossHeaders ={
    'authority': 'www.zhipin.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh,zh-CN;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control':'max-age=0',
    'cookie':'_uab_collina=154755676361575782833859; linkSignResumeNew=true; lastCity=101010100; JSESSIONID=""; __c=1548328523; __g=-; __l=l=%2Fwww.zhipin.com%2F&r=https%3A%2F%2Fwww.google.com%2F; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1548329549,1548329560,1548329774,1548330589; toUrl=http%3A%2F%2Fwww.zhipin.com%2Fc101010100-p101101%2F; __a=10508737.1547556761.1548293541.1548328523.121.6.72.121; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1548334620',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
