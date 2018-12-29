# coding=utf-8
"""
@Project: JinRong
@Time: 2018/12/28 11:29
@Name: GetMagazinePageOffset
@Author: lieyan123091
"""
import re, sys


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))

regex_tab = re.compile("\\t")


def get_magazine_pageoffset():
    with open(u"MagazineTitle.txt", "r") as f1:
        while True:
            line1 = f1.readline()
            if len(line1) < 1:
                break
            info1 = regex_tab.split(line1)
            pages = int(info1[17])
            if pages > 1:
                pageRange = info1[16]
            else:
                pageRange = info1[16] + '-' + info1[16]
            write_mapping_log("MagazinePageOffset.txt",info1[2]+"\t"+info1[3]+"\t"+pageRange+"\n")
            print info1[2] + "_" + info1[3] + " Compute Successfully ..."






def main():
    get_magazine_pageoffset()

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()