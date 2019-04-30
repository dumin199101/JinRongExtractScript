# coding=utf-8
"""
@Project: JinRong
@Time: 2019/4/29 17:28
@Name: RenameOrgName
@Author: lieyan123091
"""
import re, sys, os
import shutil

DEST_DIR = u"E:\\Goosuu\\JinRong\\Script\\Result\\Pic_Finish"

regex_tab = re.compile("\\t")

i = 1

def rename_cover(srcdir):
    global i
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
    with open(u"org_list.txt", "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            name = info[0]
            for filename in os.listdir(srcdir):
                filename = filename[:filename.rfind(".")]
                if filename == name:
                    srcfile = srcdir + "\\" + name + ".jpg"
                    desfile = (DEST_DIR + "\\" + str(i) + ".jpg").encode("gbk")
                    # os.rename(srcfile, desfile)
                    shutil.copy2(srcfile,desfile)
                    print i, srcfile
                    i = i + 1
                    continue

i = 1
set_img = set()
set_img_info = set()
regex_tab = re.compile("\\t")


def get_diff_img():
    global i
    with open(u"org_list.txt", "r") as f1:
        while True:
            line1 = f1.readline()
            if len(line1) < 1:
                break
            info1 = regex_tab.split(line1)
            set_img.add(info1[0])

    for filename in os.listdir(u"E:\\Goosuu\\JinRong\\Script\\Result\\Pic"):
            set_img_info.add(filename[:filename.rfind(".")].encode("utf-8"))

    set_diff = set_img.difference(set_img_info)
    # set_diff = set_img_info.difference(set_img)

    for obj in set_diff:
        print i,obj
        i = i + 1







def main():
    srcdir = u"E:\\Goosuu\\JinRong\\Script\\Result\\Pic"
    rename_cover(srcdir)
    # get_diff_img()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()