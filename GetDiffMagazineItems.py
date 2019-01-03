# coding=utf-8
"""
@Project: JinRong
@Time: 2018/12/27 11:45
@Name: GetDiffMagazineItems
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


set_items_pdf = set()
set_items_title = set()
regex_tab = re.compile("\\t")


def get_diff_items():
    with open(u"MagazineTitle.txt", "r") as f1:
        while True:
            line1 = f1.readline()
            if len(line1) < 1:
                break
            info1 = regex_tab.split(line1)
            set_items_pdf.add(info1[1])

    with open(u"MagazinePDF.txt", "r") as f2:
        while True:
            line = f2.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            set_items_title.add(info[0])

    set_diff = set_items_pdf.difference(set_items_title)

    for obj in set_diff:
        write_mapping_log("Delete_Magazine_Items.txt", obj+"\n")
        print obj


def main():
    get_diff_items()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()