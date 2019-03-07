# coding=utf-8
"""
@Project: JinRong
@Time: 2019/3/4 14:53
@Name: GetZhuanTiResources
@Author: lieyan123091
获取专题资源
"""

import re, sys,os,shutil

SOURCE_DIR = "J:\\Finish\\book\\ExtractPDF"
DEST_DIR = "E:\\Goosuu\\ZhuanTiResource\\PDF"
SRC_BOOK_DIR = "J:\\Finish\\book\\PDF"
DEST_BOOK_DIR = "E:\\Goosuu\\ZhuanTiResource\\BOOK"
FILE_EXT = ".pdf"

regex_tab = re.compile("\\t")

i = 1

def get_title(srcfile):
    global i
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            guid = info[0]
            bookid = info[1]
            srcfile = SOURCE_DIR + "\\" + bookid + "\\" + guid + FILE_EXT
            destfolder = DEST_DIR + "\\" + bookid
            if not os.path.exists(destfolder):
                os.makedirs(destfolder)
            destfile =  destfolder + "\\" + guid + FILE_EXT
            shutil.copy2(srcfile,destfile)
            print i,bookid + "_" + guid + " Copy..."
            i = i + 1
            # print srcfile,destfile


def get_book(srcfile):
    global i
    book_set = set()
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            bookname = info[2]
            book_set.add(bookname)

        for book in book_set:
            srcfile = SRC_BOOK_DIR + "\\" + book.decode("utf-8").encode("gbk") + FILE_EXT
            destfile = DEST_BOOK_DIR + "\\" + book.decode("utf-8").encode("gbk") + FILE_EXT
            if not os.path.exists(DEST_BOOK_DIR):
                os.makedirs(DEST_BOOK_DIR)
            shutil.copy2(srcfile, destfile)
            print i,book
            i = i + 1

















def main():
    srcfile = u"get_title.txt"
    # get_title(srcfile)
    get_book(srcfile)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
