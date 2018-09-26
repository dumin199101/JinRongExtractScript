# coding=utf-8
"""
@Project: JinRong
@Time: 2018/9/25 14:18
@Name: GetMagazineName
@Author: lieyan123091
"""
import os
import sys
import re


ROOTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))

def read_mapping_log(logname):
    """
    读取log日志
    :param logname:
    :return:
    """
    with open(logname,"r") as f1:
        regex_tab = re.compile("\\t")
        while True:
            line = f1.readline().decode("utf-8")
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            bookname = info[2]
            write_mapping_log("MagazineBookName.txt",bookname)

def get_book_name(srcdir):
    for filename in os.listdir(srcdir):
        (name,ext) = os.path.splitext(filename)
        write_mapping_log("MagazineBookName.txt",name+"\n")











def get_all_book():
    """
    获取所有的书名
    :return:
    """
    # read_mapping_log("MAGAZINE_FILE.txt")
    srcdir = u"I:\\Deal-Middle\\Magazine\\第一批数据"
    get_book_name(srcdir)



def main():
  get_all_book()



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()