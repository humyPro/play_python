#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Humy Date:2018/9/5

from bs4 import BeautifulSoup
import requests, sys

"""
    类说明：下载都市奇缘
    网站：http://m.aoxingge.com/liste/32/32349_1/
"""


class Downloader(object):

    def __init__(self):
        self.server = 'http://m.aoxingge.com'
        # self.target = 'http://m.aoxingge.com/liste/32/32349/'

        self.names = []  # 存放章节名
        self.urls = []

    # 通用方法，获取一个html对象
    def get_html(self, target):
        req = requests.get(url=target)
        req.encoding = 'GBK'
        html = req.text
        return BeautifulSoup(html, features="html.parser")

    """
        获取下载链接
    """

    def get_url(self, target):
        req = requests.get(url=target)
        req.encoding = 'GBK'
        html = req.text
        html = BeautifulSoup(html, features="html.parser")
        indexes = html.find_all('ul', class_='chapter')
        a_bf = BeautifulSoup(str(indexes[0]), features="html.parser")
        a_page = a_bf.find_all('a')
        if len(a_page) != 0:
            for a in a_page:
                url = self.server + a.get('href')
                self.urls.append(url)
                self.names.append(a.get_text())
                print(url)

        # 下一页
        div_pages = html.find_all('div', class_='page')

        div_page = BeautifulSoup(str(div_pages[0]), features="html.parser")
        a_pages = div_page.find_all('a')
        for a_page in a_pages:
            if a_page.get_text() == '下一页':
                next_page1 = self.server + a_page.get('href')
                return str(next_page1)
        return None

    """
        获取章节内容
    """

    def get_contents(self, target):
        req = requests.get(url=target)
        req.encoding = 'GBK'
        html = req.text
        html = BeautifulSoup(html, features="html.parser")
        texts = html.find_all('div', id='nr1')
        return texts[0].text.replace('\xa0' * 4, '    \n\n')

    """
       函数说明:将爬取的文章内容写入文件
       Parameters:
           name - 章节名称(string)
           path - 当前路径下,小说保存名称(string)
           text - 章节内容(string)
       Returns:
           无
    """

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == '__main__':
    dl = Downloader()
    start_target = 'http://m.aoxingge.com/liste/32/32349/'
    print('获取下载链接')
    pages = dl.get_url(start_target)
    for i in range(1):
        pages = dl.get_url(pages)
    print('《都市奇缘》开始下载...')
    count = len(dl.urls)
    print('总共有', count, '章')
    for i in range(count):
        dl.writer(dl.names[i], '都市奇缘.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write('已下载:%.3f%%' % float(i / count) + '\r')
        sys.stdout.flush()
        count = count + 1
    print('下载完毕')
