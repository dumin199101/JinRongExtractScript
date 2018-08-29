# coding=utf-8
"""
@Project: JinRong
@Time: 2018/8/28 15:53
@Name: GetDiffImg
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


set_img = set()
set_img_info = set()
regex_tab = re.compile("\\t")


def get_diff_img():
    with open(u"ALL_IMAGE_File.txt", "r") as f1:
        while True:
            line1 = f1.readline()
            if len(line1) < 1:
                break
            info1 = regex_tab.split(line1)
            set_img.add(info1[0])

    with open(u"All_Image_Info.txt", "r") as f2:
        while True:
            line = f2.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            set_img_info.add(info[0])

    set_diff = set_img.difference(set_img_info)

    for obj in set_diff:
        write_mapping_log("Delete_Img.txt", obj + "\n")
        print obj


def main():
    get_diff_img()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
