# -*- coding: utf-8 -*-
from Job import RequestConfig

'''
boss网站规律,一个岗位有10页, https://www.zhipin.com/c101010100-p100101/?page=i&ka=page-i, i == 页数
	10 开发岗位
	11产品经理岗位
    12 设计岗位
    13 媒体运营
    ...
    30 生成总监
'''

headers = RequestConfig.headers
javaURL = 'https://www.zhipin.com/c101010100-p100101/?page=1&ka=page-1' #Java岗位
#伪装浏览器发送header

page = 1
p = 100101
hud=['职位    ','最低工资 ','最高工资','职位名','地点','经验','学历','公司行业','融资阶段','公司人数','发布日期','发布人']
print('\t'.join(hud))

for i in range(100101,100101):
    html = RequestConfig.requests.get(javaURL + str(p), headers=headers)
for n in  range(1,11):
    html = RequestConfig.requests.get(javaURL+str(page), headers = headers)
    page+=1
    soup = RequestConfig.BeautifulSoup(html.text,'html.parser')
    for item in soup.find_all('div','job-primary'):
        input = []
        input.append(item.find ('div','job-title').string) #职位名

        salary = item.find('span','red').string
        salary = salary.replace('k','')
        salary = salary.split('-')
        input.append(salary[0]) #薪资起始数
        input.append(salary[1]) #薪资起始数

        #学历、经验等要求
        requirements = item.find('p').contents
        input.append(requirements[0].string if len(requirements) > 0 else 'None') #地点
        input.append(requirements[2].string if len(requirements) > 2 else 'None') #经验
        input.append(requirements[4].string if len(requirements) > 4 else 'None') #学历

        company = item.find('div','info-company').find('p').contents
        input.append(company[0].string if len(company) > 0 else 'None') #公司行业
        input.append(company[2].string if len(company) > 2 else 'None') #融资阶段
        input.append(company[4].string if len(company) > 4 else 'None') #公司人数

        input.append(item.find('div', 'info-publis').find('p').string.replace('发布于', ''))  # 发布日期
        input.append(item.find('div', 'info-publis').find('h3').contents[3].string)  # 发布人

        print('\t'.join(input))
        RequestConfig.time.sleep(1)