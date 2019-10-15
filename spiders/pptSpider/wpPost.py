# 带有自定义栏目字段的发布文章代码
# coding:utf-8
import datetime
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.methods import taxonomies
from wordpress_xmlrpc import WordPressTerm
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
import importlib, sys

importlib.reload(sys)
# sys.setdefaultencoding('utf-8')
HOMEPATH = 'D:\\PPT资源'
LEIMU = 'PPT图表'
LANMU = '包含关系'

wp = Client('http://47.112.130.142/xmlrpc.php', 'admin', 'wzy19900420')

def getDatas():
    lanmuList = open(HOMEPATH + '\\' + LEIMU + '\\' + LANMU + '\\zip_url.txt', 'r', encoding='utf-8')
    line_lanmu = lanmuList.readline().strip()

    while line_lanmu:
        line_lanmu_tuple = line_lanmu.split(';')
        postBlog(line_lanmu_tuple[0], line_lanmu_tuple[1])
        line_lanmu = lanmuList.readline().strip()

    lanmuList.close()

def postBlog(title, content):
    post = WordPressPost()
    post.title = title
    post.content = content
    post.post_status = 'publish'  # 文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布
    post.date = datetime.datetime.today()

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
            'url': content
        }]
    })
    post.custom_fields.append({  # 资源其他信息
        'key': 'wppay_info',
        'value': [{
            'title': '附件类型',
            'desc': '.rar'
        }, {
            'title': '显示比例',
            'desc': '宽屏16:9'
        }, {
            'title': '文件大小',
            'desc': '1752 KB'
        }]
    })
    post.id = wp.call(posts.NewPost(post))
    print(post.id)

if __name__ == "__main__":
    getDatas()