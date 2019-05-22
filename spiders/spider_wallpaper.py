# @author wzy
# 爬虫
# 抓包
# 向服务器发送请求
from requests import get

# 判断文件类型的第三方包 pip install filetype
from filetype import guess

# 命名文件或者目录
from os import rename

# 递归创建目录
from os import makedirs

# 判断文件是否存在
from os.path import exists

# 将已经编码的json字符串解码为Python对象
from json import loads

# 上下文管理器操作模块，使用爬虫去连接服务器的时候，当下载完成断开连接
from contextlib import closing

# 实现一个下载器
def download(file_url, file_path, now_wallpaper_count, all_wallpaper_count):
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    # 下载图片
    with closing(get(file_url, headers=headers, stream=True)) as response:
        # 单次请求的最大值
        chunk_size = 1024
        # 文件总大小 这个参数在响应头
        content_size = int(response.headers['content-length'])
        # 初始化当前传送的大小
        data_count = 0
        # 文件操作
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                # iter_content 他是迭代地获取数据
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)

                    done_block = int((data_count / content_size) * 50)
                    data_count = data_count + len(data)

                    # 当前下载百分百
                    now_percentage = (data_count / content_size) * 100
                    print('\r %s: [%s%s] %d%% %d/%d' % (file_path, '=', '=' * done_block, now_percentage, data_count, content_size), end='', flush=True )
        print('\n')
        # 下载完成后获取图片格式
        file_type = guess(file_path)
        try:
            rename(file_path, file_path + '.' + file_type.extension)
        except FileExistsError:
            print('该文件存在')
            rename(file_path, file_path + '副本.' + file_type.extension)


# 使用爬虫去获取壁纸资源
# type_id 指定地址分类，wallpaper_count指定壁纸下载张数1
def spider_wallpaper(type_id, wallpaper_count):
    # 根据地址分类，请求数据
    url = ''
    if type_id == '1':
        url = 'https://service.paper.meiyuan.in/api/v2/columns/flow/5c68ffb9463b7fbfe72b0db0?page=1&per_page=' + str(wallpaper_count)
    elif type_id == '2':
        url = 'https://service.paper.meiyuan.in/api/v2/columns/flow/sdfsds?page=1&per_page=' + str(wallpaper_count)
    elif type_id == '3':
        url = 'https://service.paper.meiyuan.in/api/v2/columns/flow/sdfsds?page=1&per_page=' + str(wallpaper_count)
    elif type_id == '4':
        url = 'https://service.paper.meiyuan.in/api/v2/columns/flow/sdfsds?page=1&per_page=' + str(wallpaper_count)

    # header 模拟浏览器向服务器发请求 ， 反爬
    header = {
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }

    response = get(url, headers=header)

    # 因为服务器的数据是json格式，Python不认识，所以要转成Python对象
    wallpaper_data = loads(response.text) # response.json() 两种方法
    print(wallpaper_data)
    print(type(wallpaper_data))

    #已经下载的壁纸张数，初始值
    now_wallpaper_count = 1

    # 所有的图片张数
    all_wallpaper_count = len(wallpaper_data)

    # 下载数据
    make_dir = ''
    for wallpaper in wallpaper_data:
        if type_id == '1':
            if not exists('./' + '最新壁纸'):
                makedirs('./' + '最新壁纸')
            make_dir = '最新壁纸'
        elif type_id == '2':
            if not exists('./' + '最热壁纸'):
                makedirs('./' + '最热壁纸')
            make_dir = '最热壁纸'
        elif type_id == '3':
            if not exists('./' + '女生壁纸'):
                makedirs('./' + '女生壁纸')
            make_dir = '女生壁纸'
        elif type_id == '4':
            if not exists('./' + '星空壁纸'):
                makedirs('./' + '星空壁纸')
            make_dir = '星空壁纸'

        print(wallpaper)
        # 准备下载的图片链接：
        file_url = wallpaper['urls']['raw']
        file_name_only = file_url.split('/')
        # 以最后一个URL参数作为文件名
        file_name_only = file_name_only[len(file_name_only) - 1]

        # 拼接下载保存路径
        file_path = './' + make_dir + '/' + file_name_only

        download(file_url, file_path, now_wallpaper_count, all_wallpaper_count)

        print('\t' + file_name_only)

        now_wallpaper_count += 1

if __name__ == '__main__':
    while True:
        print('\n\n')

        # 选择壁纸类型
        wallpaper_id = input('请输入壁纸类型：1.最新')

        while (wallpaper_id != str(1)):
            wallpaper_id = input('请输入壁纸类型：1.最新')

        wallpaper_count = input('请输入下载张数：')

        # 判断输入是否正确：
        while (int(wallpaper_count) < 1):
            wallpaper_id = input('请输入下载张数：')

        # 开始爬取
        print('正在下载4K超清壁纸：')
        spider_wallpaper(wallpaper_id, wallpaper_count)
