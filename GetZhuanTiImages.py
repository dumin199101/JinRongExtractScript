# coding=utf-8
"""
@Project: JinRong
@Time: 2019/3/18 9:45
@Name: GetZhuanTiImages
@Author: lieyan123091
"""
import re, sys,os,shutil

SOURCE_DIR = "I:\\Finish\\book\\Images"
DEST_DIR = "I:\\Finish-ZT\\2金融统计报告\\Images"


regex_tab = re.compile("\\t")

i = 1
j = 1

def get_images(srcfile):
    global i,j
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            bookid = info[0]
            srcfolder = SOURCE_DIR + "\\" + bookid
            destfolder = DEST_DIR.decode("utf-8").encode("gbk") + "\\" + bookid
            if not os.path.exists(destfolder):
                os.makedirs(destfolder)
            count = 0
            for root, dirs, files in os.walk(srcfolder):  # 遍历统计
                for each in files:
                    count += 1
            if count == 0:
                continue
            for file in os.listdir(srcfolder):
                srcfile = srcfolder + "\\" + file
                destfile =  destfolder + "\\" + file
                shutil.copy2(srcfile,destfile)
                print j,srcfile
                j = j + 1
            i = i + 1
            print i, bookid


def main():
    srcfile = u"report_book_info_guid.txt"
    get_images(srcfile)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
