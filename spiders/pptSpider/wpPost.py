# 带有自定义栏目字段的发布文章代码
# pip install python-wordpress-xmlrpc
# coding:utf-8
import datetime
import csv
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import posts, media
from wordpress_xmlrpc.methods import taxonomies
from wordpress_xmlrpc import WordPressTerm
from wordpress_xmlrpc.compat import xmlrpc_client
import importlib, sys

importlib.reload(sys)
HOMEPATH = 'D:\\PPT资源'
LEIMU = 'PPT模板'
LANMU = '动态PPT模板'

wp = Client('http://47.112.130.142/xmlrpc.php', 'admin', 'wzy19900420')

def getDatas():
    with open(HOMEPATH + '\\' + LEIMU + '\\' + LANMU + '\\zip_url.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader_lines = csv.reader(csv_file)
        index = 0
        for one_line in csv_reader_lines:
            print(one_line)
            if index != 0:
                postBlog(one_line[1], one_line[2], one_line[3], one_line[4], one_line[5], one_line[6], one_line[7])
            index += 1

def postBlog(title, content, downloadUrl, type, size, scale, attach):
    print(type)
    post = WordPressPost()
    post.title = title
    post.content = content
    post.post_status = 'publish'  # 文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布
    # post.date = datetime.datetime.today()

    post.terms_names = {
        'post_tag': [LANMU],  # 文章所属标签，没有则自动创建
        'category': [LEIMU]  # 文章所属分类，没有则自动创建
    }

    post.custom_fields = []  # 自定义字段列表
    post.custom_fields.append({  # 资源类型
        'key': 'wppay_type',
        'value': 4
    })
    post.custom_fields.append({  # 资源下载信息
        'key': 'wppay_down',
        'value': [{
            'name': '立即下载',
            'url': downloadUrl
        }]
    })
    post.custom_fields.append({  # 资源其他信息
        'key': 'wppay_info',
        'value': [{
            'title': type.split('：')[0],
            'desc': type.split('：')[1]
        }, {
            'title': size.split('：')[0],
            'desc': size.split('：')[1]
        }, {
            'title': scale.split('：')[0],
            'desc': scale.split('：')[1]
        }, {
            'title': attach.split('：')[0],
            'desc': attach.split('：')[1]
        }]
    })
    post.id = wp.call(posts.NewPost(post))
    print(post.id)

if __name__ == "__main__":
    getDatas()