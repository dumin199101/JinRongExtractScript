# coding=utf-8
"""
@Project: JinRong
@Time: 2019/2/14 15:34
@Name: GetAuthorTitleReferTest
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


def get_book_author():
    with open(u"tb_book_author.txt", "r") as f1:
        while True:
            line1 = f1.readline()
            if len(line1) < 1:
                break
            info = regex_tab.split(line1)
            bookname = info[0]
            authorname = info[1].strip("\n")
            with open(u"tmp_title_info.txt", "r") as f2:
                while True:
                    line2 = f2.readline()
                    if len(line2) < 1:
                        break
                    info1 = regex_tab.split(line2)
                    guid = info1[0]
                    title = info1[1]
                    book = info1[2].strip("\n")
                    if bookname == book:
                        print bookname
                        # write_mapping_log("AuthorTitle.txt",guid+"\t"+title+"\t"+book+"\t"+authorname+"\n")
                        write_mapping_log("AuthorTitleRefer.txt",guid+"\t"+authorname+"\n")
                    else:
                        continue



def main():
    get_book_author()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
