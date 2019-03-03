# coding=utf-8
"""
@Project: JinRong
@Time: 2019/3/2 18:12
@Name: RenameCoverFile
@Author: lieyan123091
重命名封面
"""
import re, sys, os

regex_tab = re.compile("\\t")

i = 1

def rename_cover(srcdir):
    global i
    with open(u"Txt/GUID/tb_book_info_GUID.txt", "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            guid = info[0]
            name = info[1].strip("\n")
            for filename in os.listdir(srcdir):
                if filename==(name+".jpg"):
                    srcfile = srcdir + "\\" + filename
                    desfile = srcdir + "\\" + guid + ".jpg"
                    os.rename(srcfile,desfile)
                    print i,srcfile,desfile
                    i = i + 1
                    continue










def main():
    srcdir = u"I:\\Covers"
    rename_cover(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
