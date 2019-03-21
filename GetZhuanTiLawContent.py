# coding=utf-8
"""
@Project: JinRong
@Time: 2019/3/21 16:54
@Name: GetZhuanTiLawContent
@Author: lieyan123091
"""
import os,sys,re

def del_blank_char(str):
    """
    去除字符串中的空白跟换行符
    :param str:
    :return:
    """
    rep = re.compile(r'(\n|\t|\r)')
    (fstr, count) = rep.subn('', str)
    return fstr

def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))

def get_law_content(srcfolder):
    for file in os.listdir(srcfolder):
        guid = file[:-4]
        srcfile = srcfolder + "\\" + file
        with open(srcfile,"r") as f1:
            str = f1.read()
            content = del_blank_char(str)
            # print guid,content
            write_mapping_log("law_new_content.txt",guid + "\t" + content + "\n")
            print guid




def main():
    srcfolder = u"J:\\law_title"
    get_law_content(srcfolder)



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()