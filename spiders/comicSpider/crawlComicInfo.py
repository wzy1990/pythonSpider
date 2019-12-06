# 首先爬取类别链接并创建大类文件夹
# pip install pandas
import requests
import os
import time
import pandas as pd

from numpy import *
from bs4 import BeautifulSoup as bs

URL = 'https://www.dm5.com/'
FILE = 'D:\\comic资源'
header = {
    'Referer': 'https://www.dm5.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36'
}


# 获取网页信息
def get_html(url):
    html = requests.get(url, headers=header)
    html.encoding = 'utf8'
    soup = bs(html.text, 'lxml')
    return soup


# 创建新的文件夹
def creatFile(element, FILE=FILE):
    path = FILE
    title = element
    new_path = os.path.join(path, title)
    if not os.path.isdir(new_path):
        os.makedirs(new_path)
    return new_path


# 判断文件名
def judgeName(name):
    fh = ['?', '\\', '/', '：', '*', '"', '<', '>', '|']
    for fh_ in fh:
        if fh_ in name:
            name = name.replace(fh_, '_')
    return name

# 用于爬取每个类目下的漫画信息
def CrawModel(new_path, url):

    post_list = []
    csv_title = ['标题', '作者', '封面', '内容简介', '题材类型', '评分', '更新集数', '是否完结', '最近更新时间', '下载地址']
    page_num = 1
    flag = True  # 控制跳出循环
    while True:
        if page_num == 1:
            curl = url  # 分类的第一页，可以不用构造
        else:
            curl = url + '-p' + str(page_num) # 该分类的其他页，非第一页

        try:  # 第一种URL格式，带有ppt_
            page = get_html(curl)
        except:
            flag = False
        print(time.ctime() + "; 爬取" + curl + "页")

        try:
            ul = page.find('ul', {'class': 'mh-list'})
            li = ul.find_all('li')
            i_num = 1
            for i in li:
                h2 = i.find('h2')
                href = h2.find('a')['href']
                print(time.ctime() + "; 打印第" + str(page_num) + "页第" + str(i_num) + "个漫画: " + h2.text)
                # 进入详情页
                comic_html = get_html(URL + href)
                # 漫画详情信息区域
                comic_detail = comic_html.find('div', {'class': 'banner_detail_form'})
                # 漫画标题
                comic_title = h2.find('a')['title']
                # 漫画作者
                comic_author = comic_detail.find('p', {'class': 'subtitle'}).find('a').text
                # 漫画封面
                comic_cover = comic_detail.find('div', {'class': 'cover'}).find('img')['src']
                # 漫画评分
                comic_score = comic_detail.find('span', {'class': 'score'}).text
                # 漫画内容简介
                comic_content = comic_detail.find('p', {'class': 'content'}).text
                comic_content = comic_content.replace('\u3000','').replace('\xa0','')
                # 连载状态，及分类
                comic_info_list = comic_detail.find_all('span', {'class': 'block'})
                comic_serial = comic_info_list[0].find('span').text
                comic_type = comic_info_list[1].find('span').text
                # 漫画更新集数，时间
                comic_update = comic_html.find('div', {'class': 'detail-list-title'})
                comic_episodes = comic_update.find('a').find('span').text.replace('（', '').replace('）', '')
                comic_time = comic_update.find('span', {'class': 's'}).find('span').text
                # 缓存这一条文章的全部信息，以备保存到CSV
                print(comic_title + "; " + comic_author + "; " + comic_cover + "; " + comic_content)
                print(comic_type + "; " + comic_score + "; " + comic_episodes + "; " + comic_serial + "; " + comic_time)
                post_list.append([comic_title, comic_author, comic_cover, comic_content, comic_type, comic_score, comic_episodes, comic_serial, comic_time, ''])

                time.sleep(0.4)
                i_num += 1
                ErrNum = 0
            page_num += 1
        except:
            ErrNum += 1
            if ErrNum < 3:  # 容忍度为3，通过观察很少有连续两张链接不存在的，设置为3是合理的
                page_num += 1  # 跳转到下一个链接
                continue
            else:  # 若是链接已经到达最后一个，超出容忍度后结束
                print('结束')
                break
        if not flag:
            break

    post_data = pd.DataFrame(columns=csv_title, data=post_list)
    post_data.to_csv(new_path + '\comic_list.csv',encoding='UTF-8')


def main():
    f_input_url = open('D:\\comic资源\\url.txt', 'r')
    line = f_input_url.readline().strip()
    while line:
        line_tuple = line.split(';')
        path_leimu = line_tuple[0]
        url_leimu = line_tuple[1]
        # 分类名称
        path_leimu = judgeName(path_leimu)
        # 分类文件夹
        path_cell = creatFile(path_leimu, FILE=FILE + '\\')
        print(path_leimu)
        print(path_cell)
        # 爬取模板
        CrawModel(path_cell, url_leimu)
        line = f_input_url.readline().strip()


if __name__ == "__main__":
    main()