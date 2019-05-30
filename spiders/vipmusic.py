"""
python 爬虫爬取VIP音乐解析
"""
import requests

def send_request(text):
    # 被爬取的接口
    web_url = 'https://api.imjad.cn/cloudmusic/'
    # 请求头信息
    request_header = {
        'accept': '* / *',
        'origin': 'http://www.66re.cn',
        'referer': 'http://www.66re.cn/vip/163.html',
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    # 传递的参数
    search_condition = {
        'type': 'search',
        'search_type': 1,
        'limit': 30,
        's': text,
        'offset': 0
    }
    data = requests.get(url=web_url, params=search_condition, headers=request_header)
    # 返回json/dict格式数据
    print(data.json())
    return data.json()

def formatMusic(response):
    # print(type(response))
    if response.get('result'):
        results = response['result']
        # print(type(results))
        musicList = results['songs']
        for music in musicList:
            print(music)


import requests
import json

# Create your views here.
def getMusicList():
    # 被爬取的接口
    web_url =  'http://www.ciding.fun/'  # 'https://api.imjad.cn/cloudmusic/'
    # 请求头信息
    request_header = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'host': 'www.ciding.fun',
        'origin': 'http://www.ciding.fun',
        'referer': 'http: // www.ciding.fun ',
        'cookie': 'UM_distinctid=16aed99e423eb-08aaf141275c8f-4446062d-1fa400-16aed99e42447c; CNZZDATA1273782431=475375742-1558761687-%7C1558761687',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    # 传递的参数
    search_condition = {
        'type': 'netease',
        'filter': 'name',
        'input': '黎明',
        'page': 1
    }
    print(json.dumps(search_condition))
    data = requests.post(url=web_url, json=json.dumps(search_condition), headers=request_header)
    print(data.text)
    # 返回json/dict格式数据
    response = data.json()
    if response.get('data'):
        musicList = response['data']

def saveMusic():
    pass

def main():
    search_text = input('请输入你需要查询的歌曲：') # 根据输入的关键字查找歌曲
    response = send_request(search_text) # 爬取音乐歌曲

    getMusicList() # 爬取音乐歌曲
    formatMusic(response) # 格式化输出爬取结果

main()