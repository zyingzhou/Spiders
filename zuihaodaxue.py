#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author:Zhiying Zhou
URL: www.zhouzying.cn
Date: Mar,1,2018
Description:这是爬取最好大学网近三年的中国最好大学的排名。
'''

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import time
from multiprocessing import Pool
headers = {"User-Agent": "Mozilla/5.0"}


# 通过url获取网页
def get_HTML_page(url):
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except RequestException:
        print("爬取失败！")


# 解析网页并保存数据
def parse_HTML_page(html):
    soup = BeautifulSoup(html,'html5lib')
    for tr_tags in soup.tbody.find_all('tr'):
        items = []
        for td_tag in tr_tags.find_all('td'):
            items.append(td_tag.string)
        with open("zuihaodaxue.txt",  'a') as f:
            f.write("{:<4}{:^12}{:^14}{:^18}{:^24}\n".format(items[0].strip(), items[1].strip(), items[2].strip(),
                                                             items[3].strip(), items[4].strip()))
            f.close()


def main(Y):

    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming" + str(Y) + ".html"
    html = get_HTML_page(url)
    # with open("D:\\zuihaodaxue.txt",'a') as f:
    # f.write("{}年软科中国最好大学排名\n".format(Y))
    # f.close()
    parse_HTML_page(html)


if __name__ == '__main__':
    time.clock()
    print("------开始获取数据------")
    with open("zuihaodaxue.txt",'a') as f:
        f.write("软科中国最好大学排名（2016-2018）\n{:<4}{:^12}{:^14}{:^18}{:^24}\n".format('排名', '学校名称', '省市',
                                                                                '总分', '指标得分'))
        f.close()
    p = Pool()
    p.map(main, [2016, 2017, 2018])
    print("-------数据保存成功！------")
    print("程序运行时间为{}".format(time.clock()))
    
