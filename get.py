import requests
from bs4 import BeautifulSoup
import pandas


# ggkzt 公共课真题|jjxzy 经济类专业|fxlzy 法学类专业|wxlzy 文学类专业|gxlzy 理工类专业|jyl 教育类专业|gllzy 管理类专业|nxlzy 农学类专业|yxlzy 医学类专业|qtl 其它类
url1 = 'http://www.tfzikao.com/xlks/lnst/gxlzy/'
num = 2
href_data = []
title_data = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Referer': 'http://www.tfzikao.com/xlks/lnst/',
    'host': 'Host: www.tfzikao.com',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6'
}

# 抓取第一页内容
r = requests.get(url1,headers=headers)
r.encoding = 'UTF-8'
ul_data = BeautifulSoup(r.text,'lxml').find('ul', class_='mod-list mod-list-date mod-list-long')
for i in ul_data.find_all('a'):
        href_data.append(i['href'])
        title_data.append(i['title'])
pd = pandas.DataFrame({'num':'1','url':href_data,'name':title_data})
pd.to_csv('tfzikaoDATA.csv',mode='a',header=None)
title_data.clear()
href_data.clear()

# 抓取第一页之后的内容,下行数字应为总页数+1
while num < 133:
    url = url1 + 'List_' + str(num) + '.html'
    r = requests.get(url,headers=headers)
    r.encoding = 'UTF-8'
    soup = BeautifulSoup(r.text,'lxml')
    ul_data = soup.find('ul', class_='mod-list mod-list-date mod-list-long')
    for i in ul_data.find_all('a'):
        href_data.append(i['href'])
        title_data.append(i['title'])
    num = num +1
    pd = pandas.DataFrame({'num':num,'url':href_data,'name':title_data})
    pd.to_csv('tfzikaoDATA.csv',mode='a',header=None)
    title_data.clear()
    href_data.clear()