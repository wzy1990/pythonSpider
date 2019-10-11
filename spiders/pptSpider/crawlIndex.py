import requests
import os
import time
from bs4 import BeautifulSoup

#获取网页信息
def get_html(url):
    html = requests.get(url)
    html.encoding = 'gb2312'
    soup = BeautifulSoup(html.text, 'lxml')
    return soup

#创建新的文件夹
def creatFile(element):
    path = FILEPATH
    title = element
    new_path = os.path.join(path, title)
    if not os.path.isdir(new_path):
        os.makedirs(new_path)
    return new_path

def main():
    content = get_html(URL)
    navMenu = content.find('div', {'id':'navMenu'})
    menus = navMenu.find_all('li')
    with open('D:\\PPT资源\\url.txt', 'w') as f:
        for li in menus:
            li_a = li.find('a')
            link = URL + li_a['href']
            name = li_a.text
            creatFile(name)
            f.write(name + ';' + link + '\n')
    print('结束！')
    pass


if __name__ == '__main__':
    URL = 'http://www.1ppt.com'
    FILEPATH = 'D:\\PPT资源'
    main()