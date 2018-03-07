'''Feb,25,2018 Author: Zhiying Zhou'''
from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException
import time
from multiprocessing import Pool
headers = {'User-agent':'Mozilla/5.0'}
#获取网页
def get_html_page(url):
    try:
        r = requests.get(url,headers = headers)
        r.encoding = 'utf-8'
        r.raise_for_status()
        return r.text
    except RequestException:
        print('爬取失败！')
#解析网页并保存数据
def html_page_paser(html):
    soup = BeautifulSoup(html,'html5lib')
    for dd_tag in soup.find_all('dd'):
        items = []   #创建一个列表来存储数据
        for p_tag in dd_tag.find_all('p'):
            items.append(p_tag.string)
            #开始写入到本地文件
        with open("D:\\maoyan_top100_films_results1.txt",'a',encoding='utf-8') as f:
            f.write(dd_tag.i.string + '  ' + items[0].strip() + '  ' + items[1].strip() + '  ' + items[2].strip() + \
                    '    '+ 'http://maoyan.com' + dd_tag.p.a['href'] + '\n')
            f.close()

def main():
    for i in range(10):
        i = i * 10
        url = "http://maoyan.com/board/4?offset=" + str(i)
        html = get_html_page(url)
        html_page_paser(html)
if __name__ == '__main__':
    #开始计算程序运行的时间
    p = Pool(10)
    time.clock()
    print("...开始爬取数据...\n......请稍等......")
    main()
    print('Success!')
    print("程序运行时间:{}".format(time.clock()))






