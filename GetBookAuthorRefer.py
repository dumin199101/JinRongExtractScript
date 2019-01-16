# coding=utf-8
"""
@Project: JinRong
@Time: 2019/1/16 9:51
@Name: GetBookAuthorRefer
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
    with open(u"tb_book_info.txt", "r") as f1:
        while True:
            line1 = f1.readline()
            if len(line1) < 1:
                break
            info = regex_tab.split(line1)
            author_info = info[1]
            if author_info.rfind(",") > -1 or author_info.rfind("、")>-1:
                if author_info.rfind(",") > -1:
                    authors = author_info.split(",")
                elif author_info.rfind("、")>-1:
                    authors = author_info.split("、")
                for author in authors:
                    write_mapping_log("book_author_refer.txt",info[0]+"\t"+author+"\n")
            else:
                write_mapping_log("book_author_refer.txt", info[0] + "\t" + author_info + "\n")





def main():
    get_book_author()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()