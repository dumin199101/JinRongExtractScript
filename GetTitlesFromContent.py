# coding=utf-8
"""
@Project: JinRong
@Time: 2018/9/26 16:46
@Name: GetTitlesFromContent
@Author: lieyan123091
"""
import re

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
            # if len(info) < 6:
            #     print info
            #     for str in info:
            #         print str
            str = info[1] + "\t" + info[0] + "\t" + info[5] + "\n"
            write_mapping_log("GetTitle.txt", str)
            print info[0] + "_" + info[1]





if __name__ == '__main__':
    read_mapping_log("E:\\Goosuu\\JinRong\\Script\\Check_Content_File.txt")