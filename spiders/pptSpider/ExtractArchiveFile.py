import zipfile
import os
from unrar import rarfile


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


# 解压缩文件
def archive_extract(zip_exit_file, one_file, two_file):  # zip文件所在目录，主题文件夹，类别文件夹
    current_file_path = 'F://ppt1//' + one_file + '//' + two_file + '//'  # 用于创建新的主题文件夹和类别文件夹
    current_file_names = os.listdir(zip_exit_file)  # 压缩文件所在的类别文件夹下的所有文件
    for current_file_name in current_file_names:
        print(current_file_name)
        archive_format = current_file_name[current_file_name.find('.'):]  # 压缩文件格式
        archive_name = current_file_name[:current_file_name.find('.')]  # 压缩文件名称
        if archive_format == '.zip':  # 判断压缩文件类型，不同的类型解压所用的包不同
            azip = zipfile.ZipFile(zip_exit_file + current_file_name, 'r')  # 读取压缩包里面的文件
            try:
                zip_num = 1  # 如果压缩文件中有多个文件，命名以此加1
                for filename in azip.namelist():  # 遍历所有文件
                    #                     print('---'+filename)
                    filename_lenth = len(filename)
                    file_format = filename[filename.find('.', filename_lenth - 5):]  # 提取压缩文件中子文件的格式
                    #                 print(file_format)
                    if file_format in ['.pptx', '.ppt', '.jpg', 'JPG']:  # 判断是否是需要的文件，如果是则解压到指定文件夹

                        try:
                            azip.extract(filename, path=current_file_path)  # 解压
                        except:
                            continue
                        if zip_num == 1:  # 首个文件命名格式
                            os.rename(current_file_path + filename, current_file_path + archive_name + file_format)
                            zip_num += 1
                        else:  # 如果是多个文件，命名加1
                            os.rename(current_file_path + filename,
                                      current_file_path + archive_name + str(zip_num) + file_format)
                            zip_num += 1
            finally:
                pass
            azip.close()
        if archive_format == '.rar':
            arar = rarfile.RarFile(zip_exit_file + current_file_name, 'r')
            try:
                rar_num = 1
                for filename in arar.namelist():
                    #                 print(filename)
                    filename_lenth = len(filename)
                    file_format = filename[filename.find('.', filename_lenth - 5):]
                    if file_format in ['.pptx', '.ppt', '.jpg', 'JPG']:
                        try:
                            arar.extract(filename, path=current_file_path)
                        except:
                            continue
                        if rar_num == 1:
                            os.rename(current_file_path + filename, current_file_path + archive_name + file_format)
                            rar_num += 1
                        else:
                            os.rename(current_file_path + filename,
                                      current_file_path + archive_name + str(rar_num) + file_format)
                            rar_num += 1
            #                 break
            finally:
                pass
    #     break
    print('结束')


def main():
    with open('F://ppt//url.txt', 'r') as f_root_url:
        zhu_ti_names = f_root_url.readlines()
    for zhu_ti_item in zhu_ti_names:
        print("正在处理" + zhu_ti_item.strip() + '_文件夹下的内容')
        zhu_ti_name = split_(zhu_ti_item)[0]  # 提取主题名
        try:
            with open('F://ppt//' + zhu_ti_name + '//url.txt', 'r') as f:
                lei_bie_names = f.readlines()
            for lei_bie_item in lei_bie_names:
                print("   正在解压" + lei_bie_item.strip() + "_类别下的压缩文件")
                lei_bie_name = judgeName(split_(lei_bie_item)[0])
                extract_file = 'F://ppt//' + zhu_ti_name + '//' + lei_bie_name + '//'  # 压缩文件所在位置
                archive_extract(extract_file, zhu_ti_name, lei_bie_name)
        except:
            with open('F://ppt//' + zhu_ti_name + '//url.txt', 'r', encoding='utf-8') as f:
                lei_bie_names = f.readlines()
            for lei_bie_item in lei_bie_names:
                print("   正在解压" + lei_bie_item.strip() + "_类别下的压缩文件")
                lei_bie_name = judgeName(split_(lei_bie_item)[0])
                extract_file = 'F://ppt//' + zhu_ti_name + '//' + lei_bie_name + '//'  # 压缩文件所在位置
                archive_extract(extract_file, zhu_ti_name, lei_bie_name)


if __name__ == "__main__":
    main()