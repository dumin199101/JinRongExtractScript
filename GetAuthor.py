# coding=utf-8
"""
@Project: JinRong
@Time: 2019/1/10 17:57
@Name: GetAuthorTest
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


set_author = set()
set_editor = set()
regex_tab = re.compile("\\t")


def get_author():
    with open(u"tb_book_info.txt", "r") as f1:
        while True:
            line1 = f1.readline()
            if len(line1) < 1:
                break
            info = regex_tab.split(line1)
            author_info = info[1]
            editor_info = info[2]
            if author_info.rfind(",") > -1 or author_info.rfind("、")>-1:
                if author_info.rfind(",") > -1:
                    authors = author_info.split(",")
                elif author_info.rfind("、")>-1:
                    authors = author_info.split("、")
                for author in authors:
                    set_author.add(author)
            else:
                set_author.add(author_info)
            if editor_info.rfind(",") > -1 or editor_info.rfind("、")>-1:
                if editor_info.rfind(",") > -1:
                    editors = editor_info.split(",")
                elif editor_info.rfind("、") > -1:
                    editors = editor_info.split("、")
                for editor in editors:
                    set_editor.add(editor.strip("\n"))
            else:
                set_editor.add(editor_info.strip("\n"))
    for author in set_author:
        print author
    print "*" * 100
    for editor in set_editor:
        print editor




def main():
    get_author()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()