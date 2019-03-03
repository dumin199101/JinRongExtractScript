# coding=utf-8
"""
@Project: JinRong
@Time: 2019/2/27 17:42
@Name: GetBookCatecoryStr
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
    根据MULU_File.txt计算目录层级，得出下级目录的上级目录名称，并形成参照文件MULU_Level_File.txt
    :param logname:
    :return:
    """
    with open(logname, "r") as f1:
        regex_tab = re.compile("\\t")
        i = 1
        while True:
            line = f1.readline().decode("utf-8")
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            bookname = info[0]
            cat_1 = info[1]
            cat_2 = info[2]
            cat_3 = info[3]
            cat_4 = info[4]
            cat_str = cat_1 + "," + cat_2
            if len(cat_3.strip()) > 0:
                cat_str = cat_str + "," + cat_3
            if len(cat_4.strip()) > 0:
                cat_str = cat_str + "," + cat_4
            industry = info[5].strip("\n")
            print i,bookname,cat_str,industry
            write_mapping_log("cate_industry_mapping.txt",bookname+"\t"+cat_str+"\t"+industry+"\n")
            i = i + 1











def get_category_name():
    read_mapping_log("category.txt")



def main():
  get_category_name()



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()