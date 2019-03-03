# coding=utf-8
"""
@Project: JinRong
@Time: 2019/3/3 12:01
@Name: GetTotalPages
@Author: lieyan123091
"""
import re, sys, os

regex_tab = re.compile("\\t")

sum = 0
i = 1

def get_total_pages():
    global i,sum
    with open(u"pages.txt", "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            page = info[0].strip("\n")
            sum = sum + int(page)
            print i, page, sum
            i = i + 1











def main():
    get_total_pages()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()