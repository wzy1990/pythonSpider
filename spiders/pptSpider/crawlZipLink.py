# 首先爬取类别链接并创建大类文件夹
import requests
import os
import time
from bs4 import BeautifulSoup as bs

URL = 'http://www.1ppt.com/'
FILE = 'D:\\PPT资源'
header = {
    'Referer': 'http://www.1ppt.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36'
}


# 获取网页信息
def get_html(url):
    html = requests.get(url, headers=header)
    html.encoding = 'gb2312'
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


def CrawModel(new_path, url):
    # 用于爬取每个类目下的ppt模板\

    f = open(new_path + '\zip_url.txt', 'w', encoding='utf-8')
    page_num = 1
    flag = True  # 控制跳出循环
    while True:
        struct_url = url.split('/')[-1]
        if page_num == 1:
            curl = url  # 分类的第一页，可以不用构造
        else:
            curl = url + '/ppt_' + struct_url + '_' + str(page_num) + '.html' # 该分类的其他页，非第一页

        try:  # 第一种URL格式，带有ppt_
            page = get_html(curl)
        except:
            try: # 第二种URL格式，没有ppt_
                curl = url + '/' + struct_url + '_' + str(page_num) + '.html'
                page = get_html(curl)

            except:  # 其他情况，有时间再搞
                # curl = url
                # page = get_html(curl)
                flag = False
        print(time.ctime() + ";爬取" + curl + "页")
        try:
            ul = page.find('ul', {'class': 'tplist'})
            li = ul.find_all('li')
            i_num = 1
            for i in li:
                print(time.ctime() + ";打印第" + str(page_num) + "页第" + str(i_num) + "个ppt")
                h2 = i.find('h2')
                href = h2.find('a')['href']
                name = h2.text
                zip_content = get_html(URL + href)
                zip_href = zip_content.find('ul', {'class': 'downurllist'}).find('a')['href']
                f.write(name + ';' + zip_href + '\n')
                time.sleep(0.2)
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
    f.close()


def main():
    f_input_url = open('D:\\PPT资源\\url.txt', 'r')
    line = f_input_url.readline().strip()
    while line:
        line_tuple = line.split(';')
        path_leimu = line_tuple[0]
        url_leimu = line_tuple[1]
        # 一行,创建每个类目下的栏目文件夹
        f_input_lanmu = open(FILE + '\\' + path_leimu + '\\url.txt', 'r')
        line_lanmu = f_input_lanmu.readline().strip()
        while line_lanmu:
            line_lanmu_tuple = line_lanmu.split(';')
            path_lanmu = line_lanmu_tuple[0]
            url_lanmu = line_lanmu_tuple[1]
            print(FILE + '\\' + path_leimu + '\\' + path_lanmu, url_lanmu)
            # print('------'+path_lanmu)
            path_lanmu = judgeName(path_lanmu)
            path_cell = creatFile(path_lanmu, FILE=FILE + '\\' + path_leimu + '\\')
            # 爬取模板
            CrawModel(path_cell, url_lanmu)
            # print(path_cell)
            line_lanmu = f_input_lanmu.readline().strip()
        f_input_lanmu.close()
        line = f_input_url.readline().strip()


if __name__ == "__main__":
    main()