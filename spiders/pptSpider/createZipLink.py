#打开类目url，选中文件夹
def split_(string):
    st = string.strip().split(';')
    return st
#处理文件夹名称
def judgeName(name):
    fh = ['?','\\','/','：','*','"','<','>','|']
    for fh_ in fh:
        if fh_ in name:
            name = name.replace(fh_, '_')
    return name
def main():
    f_input = open("D:\\PPT资源\\url.txt", 'r')
    leimus = f_input.readlines()
    # print(leimus)
    f_input.close()
    for leimu in leimus:
        if leimu.strip():
            leimu_= split_(leimu)
            leimu_name = leimu_[0]#提取类目文件夹
    #         print(file_name)
            f_lanmu = open("D:\\PPT资源\\"+leimu_name+'\\url.txt','r')
            lanmus = f_lanmu.readlines()
            for lanmu in lanmus:
                if lanmu.strip():
                    lanmu_ = split_(lanmu)
                    lanmu_name = judgeName(lanmu_[0])
                    lanmu_link = lanmu_[1]
    #                 print(lanmu_name)
                    with open("D:\\PPT资源\\"+leimu_name+'\\'+lanmu_name+'\\zip_url.txt','r',encoding='utf-8') as f_zip:
                        with open("D:\\PPT资源\\"+leimu_name+'\\'+lanmu_name+'\\zip.txt','w',encoding='utf-8') as f_output:
                            zipUrls = f_zip.readlines()
                            for zipUrl in zipUrls:
                                zipUrl = split_(zipUrl)
                                zip_link = zipUrl[1]
                                f_output.write(zip_link+'\n')
                    print("正在处理"+leimu_name+";"+lanmu_name)
    #                 print('over!')
    print("结束")
if __name__ == "__main__":
    main()