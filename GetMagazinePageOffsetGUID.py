# coding=utf-8
"""
@Project: JinRong
@Time: 2019/1/7 10:18
@Name: GetMagazinePageOffsetGUID
@Author: lieyan123091
"""

import re
import sys


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))

regex_tab = re.compile("\\t")

def get_magazine_pageoffset():
    with open(u"MagazinePageOffset.txt", "r") as f1:
        while True:
            line1 = f1.readline()
            if len(line1) < 1:
                break
            info1 = regex_tab.split(line1)
            write_mapping_log("MagazinePageOffsetGUID.txt",info1[0] + "_" + info1[1] + "\t" + info1[0]+"\t"+info1[1]+"\t"+info1[2])
            print info1[0] + "_" + info1[1] + " Generate Successfully ..."






def main():
    get_magazine_pageoffset()

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()