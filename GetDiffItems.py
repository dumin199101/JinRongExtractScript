# coding=utf-8
"""
@Project: JinRong
@Time: 2018/9/27 11:32
@Name: GetDiffItems
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


set_items = set()
set_items_info = set()
regex_tab = re.compile("\\t")


def get_diff_items():
    with open(u"Check_Page_Offset_File.txt", "r") as f1:
        while True:
            line1 = f1.readline()
            if len(line1) < 1:
                break
            info1 = regex_tab.split(line1)
            set_items.add(info1[5])

    with open(u"GetTitle.txt", "r") as f2:
        while True:
            line = f2.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            set_items_info.add(info[2])

    set_diff = set_items.difference(set_items_info)

    for obj in set_diff:
        write_mapping_log("Delete_Items.txt", obj)
        print obj


def main():
    get_diff_items()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()