import os


# 打开类目url，选中文件夹
def split_(string):
    st = string.strip().split(';')
    return st


# 处理文件夹名称
def judgeName(name):
    fh = ['?', '\\', '/', '：', '*', '"', '<', '>', '|']
    for fh_ in fh:
        if fh_ in name:
            name = name.replace(fh_, '_')
    return name


# 传入一个当前文件夹名称，对其子文件进行更改名称
def change_file_name(current_file_path):  # 变量格式：'F://ppt//中国风背景图片//'
    print("正在更改" + current_file_path + "文件夹下的内容")
    current_file_names = os.listdir(current_file_path)
    if len(current_file_names) > 2:
        f = open(current_file_path + 'zip_url.txt', 'r', encoding='utf-8')
        current_zip_url_names = f.readlines()
        f.close()
        for current_file_name in current_file_names:
            file_format = current_file_name[current_file_name.find("."):]  # 读取当前文件格式

            # 读取文件名称
            file_name = current_file_name[:current_file_name.find(".")]
            # 在zip_url文件中遍历
            for zip_url_name in current_zip_url_names:
                zip_url_name = split_(zip_url_name)
                zip_name = zip_url_name[0]
                #         print(name)
                zip_url = zip_url_name[1]
                file_real_name = zip_url.split('/')[-1][:zip_url.split('/')[-1].find(".")]  # 在zip_url中的链接中找到压缩文件名
                if file_name == file_real_name:
                    try:
                        if file_format == '.rar':  # 判断格式，精确重命名，后面文件批量解压不同的格式有不同的方法。
                            os.rename(current_file_path + file_name + '.rar', current_file_path + zip_name + '.rar')
                        else:
                            os.rename(current_file_path + file_name + '.zip', current_file_path + zip_name + '.zip')
                    except:
                        pass
                else:
                    pass


def main():
    with open('F://ppt//url.txt', 'r') as f_root_url:
        zhu_ti_names = f_root_url.readlines()
    for zhu_ti_item in zhu_ti_names:
        print("正在处理" + zhu_ti_item + '_文件夹下的内容')
        zhu_ti_name = split_(zhu_ti_item)[0]  # 提取主题名
        with open('F://ppt//' + zhu_ti_name + '//url.txt', 'r') as f:
            lei_bie_names = f.readlines()
        for lei_bie_item in lei_bie_names:
            lei_bie_name = judgeName(split_(lei_bie_item)[0])
            change_file_name('F://ppt//' + zhu_ti_name + '//' + lei_bie_name + '//')


if __name__ == "__main__":
    main()