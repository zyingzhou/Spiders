# Ajax loading
import requests


# 分析Ajax接口得到url
url = 'https://www.topuniversities.com/sites/default/files/qs-rankings-data/357051.txt?_=1525068930958'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 "
                         "Safari/537.36"}


# 获取数据
def get_page(url):
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.json()
    except requests.ConnectionError as e:
        print(e)


# 解析数据
def parser_page(json):
    if json:
        items = json.get('data')
        for i in range(len(items)):
            item = items[i]
            qsrank = {}
            if "=" in item['rank_display']:
                rk_str = str(item['rank_display']).split('=')[-1]
                qsrank['rank_display'] = rk_str
            else:
                qsrank['rank_display'] = item['rank_display']
            qsrank['title'] = item['title']
            qsrank['region'] = item['region']
            qsrank['score'] = item['score']
            # url可根据需求提取
            qsrank['url'] = item['url']
            yield qsrank


# 主函数
def main():
    json = get_page(url)
    results = parser_page(json)
    for result in results:
        with open('/home/zhiying/文档/QSranktest.txt', 'a') as f:
            f.write('{:10}{:50}{:^88}{:>}\n'.format(result['rank_display'], result['title'], result['region'],
                                                     result['score']))
            f.close()


if __name__ == '__main__':
    print('开始获取！')
    with open('/home/zhiying/文档/QSranktest.txt', 'a') as f:
        f.write('{:^140}\n\n{:10}{:50}{:^70}{:>8}\n'.format('2018年QS全球大学排名', '排名', '大学名称', '所属国家或地区',
                                                           '得分'))
        f.close()
    main()
    print('QS大学排名获取成功！')
