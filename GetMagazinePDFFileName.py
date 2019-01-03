# coding=utf-8
"""
@Project: JinRong
@Time: 2019/1/2 17:26
@Name: GetMagazinePDFFileName
@Author: lieyan123091
"""
import os
import sys
import re

ROOTDIR = "I:\\Deal-Middle"
RESULTDIR = ROOTDIR + "\\MagazinePDF\\"
FILE_PDF_EXTENSION = ".pdf"

re_digits = re.compile(r'(\d+)')


def emb_numbers(s):
    pieces = re_digits.split(s)
    pieces[1::2] = map(int, pieces[1::2])
    return pieces


def sort_strings_with_emb_numbers2(alist):
    return sorted(alist, key=emb_numbers)


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))


# 配置数据
def get_all_magazine_files_from_dir(srcdir):
    """
    提取所有期刊数据的PDF源文件，文件名重命名为当前文件夹名，并形成参照文件MAGAZINE_PDF_FILE.txt
    :param srcdir:
    :return:
    """
    for filename in sort_strings_with_emb_numbers2(os.listdir(srcdir)):
        file = os.path.join(srcdir, filename)
        if os.path.isdir(file):
            get_all_magazine_files_from_dir(file)
        else:
            if filename.endswith(".pdf"):
                (filepath, name) = os.path.split(file)
                year_and_month = filepath[filepath.rfind("\\") + 1:]
                cat_dir = os.path.dirname(os.path.dirname(filepath))[os.path.dirname(os.path.dirname(filepath)).rfind("\\")+1:]
                write_mapping_log("MagazinePDF.txt", cat_dir + year_and_month+"_" +filename[:-4] + "\t" + file + "\t" + filename + "\n")

def main():
    # 配置数据
    srcdir = u"I:\\Deal-Middle\\ExtractMagazinePDF\\第一批数据"
    get_all_magazine_files_from_dir(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()