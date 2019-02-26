# coding=utf-8
"""
@Project: JinRong
@Time: 2019/2/12 16:33
@Name: GetAllImageFromReferDatabase
@Author: lieyan123091
从数据库中提取图片
"""
import os
import sys
import shutil
import re


FINISH_DIR = "J:\\Finish\\期刊数据\\Images\\"
SOURCE_DIR = "J:\\Deal-Middle\\期刊数据\\Book_Image\\期刊\\"

regex_tab = re.compile("\\t")

def get_all_image_files():
    with open(u"tb_magazine_image_info.txt", "r") as f1:
        while True:
            line1 = f1.readline()
            if len(line1) < 1:
                break
            info = regex_tab.split(line1)
            bookname = info[0]
            filename = info[1].strip("\n")
            destfolder = (FINISH_DIR + bookname).encode("gbk")
            if not os.path.exists(destfolder):
                os.makedirs(destfolder)
            file = (SOURCE_DIR + bookname).encode("gbk") + "\\" + filename
            destfile = destfolder + "\\" + filename
            shutil.copy2(file, destfile)
            print bookname+"_"+filename + " Copy Finished..."



def main():
    get_all_image_files()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()




