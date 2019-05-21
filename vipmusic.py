"""
python 爬虫爬取VIP音乐解析
"""
import requests
from lxml import etree

def send_request(text):
    web_url = 'https://api.imjad.cn/cloudmusic/'
    request_header = {
        'accept': '* / *',
        'origin': 'http://www.66re.cn',
        'referer': 'http://www.66re.cn/vip/163.html',
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    search_condition = {
        'type': 'search',
        'search_type': 1,
        'limit': 30,
        's': text,
        'offset': 0
    }
    data = requests.get(url=web_url, params=search_condition, headers=request_header)
    print(data.text)
    print(data.content)
    return data.text

def formatMusic(response):
    print(type(response))
    if response.get('result'):
        results = response['result']
        musicList = results.songs
        for music in musicList:
            print(music)


def saveMusic():
    pass

def main():
    search_text = input('请输入你需要查询的歌曲：')
    response = send_request(search_text)
    formatMusic(eval(response))

main()