#! /usr/bin/env python
# -*- coding: "UTF-8" -*-
"""
Author: zhiying
URL: www.zhouzying.cn
Date: 2018-12-09
Description: 浙江大学苏德矿(矿爷)微积分课程视频爬虫。课程在浙大官网。
"""
import requests
from bs4 import BeautifulSoup


def gen(uri):
    index = 0

    # uri = "//live.v.zju.edu.cn//vod/complete/201504/29/1430286933SD.mp4"
    while True:

        url = 'http:' + uri + '/' + 'av-s3-' + str(index) + '.f4v'
        headers = {'Accept': '*/*',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'Cache-Control': 'no-cache',
                   'Connection': 'keep-alive',
                   'Cookie': 'buid=ali01-1540118258168-28; Hm_lvt_fe30bbc1ee45421ec1679d1b8d8f8453=1540118925,'
                             '1540357779,1540377987; Hm_lpvt_fe30bbc1ee45421ec1679d1b8d8f8453=1540377987',
                   'Host': 'live.v.zju.edu.cn',
                   'Pragma': 'no-cache',
                   'Referer': 'http://metc.zju.edu.cn/mooc/link/wjf123.jsp?id=wjf1',
                   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.'
                                 '3497.100 Safari/537.36X-Requested-With: ShockwaveFlash/31.0.0.122'}

        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            if r.content:
                print("视频片段{}请求完成".format(index))
                index += 1
                yield r.content
        else:
            break


def get_mp4(path, uri):

    c_path = path + ".mp4"
    with open(c_path, 'ab') as f:
        for chunked_video in gen(uri):
            if chunked_video is not None:
                f.write(chunked_video)
            else:
                f.close()


def get_courses(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html5lib')
    c_name = soup.find('div', {"class": "wenzinav"}).text.strip()
    name = c_name.split('>')[-1].strip()
    # 文件路径,此方法有的文件名中会缺失第几节
    # path = name.split(' ')[0] + '/' + name.split(' ')[-1]
    # 文件路径
    if 'http://metc.zju.edu.cn/mooc/link/wjf123.jsp?id=wjf2_' in url:
        path = name.split(' ')[0] + '/' + name.split('微积分二')[-1]
    elif 'http://metc.zju.edu.cn/mooc/link/wjf123.jsp?id=wjf3_' in url:
        path = name.split(' ')[0] + '/' + name.split('微积分三')[-1]
    else:
        path = name.split(' ')[0] + '/' + name.split('微积分一')[-1]
    c_uri = soup.embed["src"].split(':')[-1]
    # 文件uri
    uri = c_uri.split('complete')[0] + '/vod/complete' + c_uri.split('complete')[-1]
    return path, uri


def main():
    # 微积分一是1-90
    # url1 = 'http://metc.zju.edu.cn/mooc/link/wjf123.jsp?id=wjf1'
    # i =7 有问题，未下载。命名错误，名字中包含非法字符
    i = 1
    print("***************开始获取微积分一课程视频***************")
    while i <= 90:
        # 微积分一是1-90
        url1 = 'http://metc.zju.edu.cn/mooc/link/wjf123.jsp?id=wjf' + str(i)
        path, uri = get_courses(url1)
        name = path.split('/')[-1]
        print("正在下载微积分一 {}".format(name))
        get_mp4(path, uri)
        print("{}  获取完成！\n".format(name))
        i += 1

    # 微积分二是1-42
    # url2 = 'http://metc.zju.edu.cn/mooc/link/wjf123.jsp?id=wjf2_01'
    j = 1
    print("***************开始获取微积分二课程视频***************")
    while j <= 42:
        # 微积分二是1-42
        if j <= 9:
            url2 = 'http://metc.zju.edu.cn/mooc/link/wjf123.jsp?id=wjf2_0' + str(j)
            path, uri = get_courses(url2)
            name = path.split('/')[-1]
            print("正在下载微积分二 {}".format(name))
            get_mp4(path, uri)
            print("微积分二 {}  获取完成！\n".format(name))
        else:
            url2 = 'http://metc.zju.edu.cn/mooc/link/wjf123.jsp?id=wjf2_' + str(j)
            path, uri = get_courses(url2)
            name = path.split('/')[-1]
            print("正在下载微积分二 {}".format(name))
            get_mp4(path, uri)
            print("微积分二 {}  获取完成！\n".format(name))
        j += 1

    # 微积分三是1-36
    # url3 = 'http://metc.zju.edu.cn/mooc/link/wjf123.jsp?id=wjf3_01'
    m = 1
    print("***************开始获取微积分三课程视频***************")
    while m <= 36:
        # 微积分三是1-36
        if m <= 9:
            url2 = 'http://metc.zju.edu.cn/mooc/link/wjf123.jsp?id=wjf3_0' + str(m)
            path, uri = get_courses(url2)
            name = path.split('/')[-1]
            print("正在下载微积分三 {}".format(name))
            get_mp4(path, uri)
            print("微积分三 {}  获取完成！\n".format(name))
        else:
            url2 = 'http://metc.zju.edu.cn/mooc/link/wjf123.jsp?id=wjf3_' + str(m)
            path, uri = get_courses(url2)
            name = path.split('/')[-1]
            print("正在下载微积分三 {}".format(name))
            get_mp4(path, uri)
            print("微积分三 {}  获取完成！\n".format(name))
        m += 1


if __name__ == '__main__':
    main()
