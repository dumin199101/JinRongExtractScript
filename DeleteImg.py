# coding=utf-8
"""
@Project: JinRong
@Time: 2018/8/28 17:05
@Name: DeleteImg
@Author: lieyan123091
"""

import sys
import os

ROOTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))
DEAL_MIDDILE_DIR = ROOTDIR + "\\Deal-Middle\\"
BookImage_DIR = DEAL_MIDDILE_DIR + "Book_Image\\"





def delete_img():
    with open(u"Delete_Img.txt", "r") as f1:
        while True:
            line = f1.readline().strip()
            if len(line) < 1:
                break
            bookname = line[:line.find("_")]
            picname =  line[line.find("_")+1:]
            destfile = BookImage_DIR + "第一批数据\\" + bookname + "\\" + picname
            os.remove(destfile.encode("gbk"))
            print destfile + " Delete..."



def main():
    delete_img()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
