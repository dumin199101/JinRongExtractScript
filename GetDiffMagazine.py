# coding=utf-8
"""
@Project: JinRong
@Time: 2018/12/27 15:07
@Name: GetDiffMagazine
@Author: lieyan123091
"""
import sys

set_items_pdf = set()

def get_magazine():
    with open(u"Delete_Magazine_Items.txt", "r") as f1:
        while True:
            line1 = f1.readline()
            if len(line1) < 1:
                break
            set_items_pdf.add(line1[:line1.rfind("_")])

    for obj in set_items_pdf:
        print obj.strip()


def main():
    get_magazine()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()


