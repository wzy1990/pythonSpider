# Python通过xmlrpc批量产生WordPress文章
import datetime
import xmlrpc.client

# WordPress站点xmlrpc地址
wp_url = "http://47.112.130.142/xmlrpc.php"
# WordPress站点管理员账号，密码
wp_username = "admin"
wp_password = "wzy19900420"
# 与WordPress服务器建立连接
server = xmlrpc.client.ServerProxy(wp_url)

HOMEPATH = 'D:\\PPT资源'
LEIMU = 'PPT图表'
LANMU = '包含关系'

def getDatas():
    lanmuList = open(HOMEPATH + '\\' + LEIMU + '\\' + LANMU + '\\zip_url.txt', 'r', encoding='utf-8')
    line_lanmu = lanmuList.readline().strip()

    while line_lanmu:
        line_lanmu_tuple = line_lanmu.split(';')
        postBlog(line_lanmu_tuple[0], line_lanmu_tuple[1])
        line_lanmu = lanmuList.readline().strip()

    lanmuList.close()

def postBlog(title, content):
    wp_blogid = ""
    publish = True
    today = datetime.datetime.today()
    date_created = xmlrpc.client.DateTime(today)
    categories = [LEIMU]
    tags = [LANMU]
    data = {
        'title': title,
        'description': content,
        'dateCreated': date_created,
        'categories': categories,
        'mt_keywords': tags
    }

    # 调用接口创建文章，如果有blogID则是编辑
    post_id = server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, publish)
    print(post_id)

if __name__ == "__main__":
    getDatas()