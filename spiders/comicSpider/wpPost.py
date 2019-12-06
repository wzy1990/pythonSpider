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
HOMEPATH = 'D:\\comic资源'
LEIMU = '港台漫画'
BEGIN = 2 # 第几行开始

wp = Client('http://47.112.130.142/xmlrpc.php', 'admin_wzy', 'admin_wzy19900420')

def getDatas():
    with open(HOMEPATH + '\\' + LEIMU + '\\zip_url.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader_lines = csv.reader(csv_file)
        index = 1
        for new_blog in csv_reader_lines:
            print(new_blog)
            if index >= BEGIN:
                postBlog(new_blog)
            index += 1

def postBlog(new_blog):
    post = WordPressPost()
    post.title = new_blog[1]
    post.post_status = 'publish'  # 文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布
    # post.date = new_blog[8]

    post.content = new_blog[4].replace('\u3000','').replace('\xa0','')

    post.terms_names = {
        'post_tag': ['rx'],  # 文章所属标签，没有则自动创建
        'category': ['gtmh']  # 文章所属分类，没有则自动创建
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
            'url': new_blog[10]
        }]
    })
    post.custom_fields.append({  # 资源其他信息
        'key': 'wppay_info',
        'value': [{
            'title': '题材类型',
            'desc': new_blog[5]
        }, {
            'title': '评分信息',
            'desc': new_blog[6]
        }, {
            'title': '更新集数',
            'desc': new_blog[7]
        }, {
            'title': '是否完结',
            'desc': new_blog[8]
        }, {
            'title': '最近更新时间',
            'desc': new_blog[8]
        }]
    })
    post.id = wp.call(posts.NewPost(post))
    print(post.id)


# 新建标签
# tag = WordPressTerm()
# tag.taxonomy = 'post_tag'
# tag.name = 'My New Tag12'  # 标签名称
# tag.slug = 'bieming12'  # 标签别名，可以忽略
# tag.id = wp.call(taxonomies.NewTerm(tag))  # 返回的id
#
# # 新建分类
# cat = WordPressTerm()
# cat.taxonomy = 'category'
# cat.name = 'cat1'  # 分类名称
# cat.slug = 'bieming2'  # 分类别名，可以忽略
# cat.id = wp.call(taxonomies.NewTerm(cat))  # 新建分类返回的id

if __name__ == "__main__":
    getDatas()