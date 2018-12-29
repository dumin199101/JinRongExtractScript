# coding=utf-8
"""
@Project: JinRong
@Time: 2018/12/28 11:21
@Name: GenMagazineFile
@Author: lieyan123091
"""
import os
import sys
import re
from pyPdf import PdfFileWriter, PdfFileReader

ROOTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))
SCRIPTDIR = "E:\\Goosuu\\JinRong\\Script"
RESULTDIR = "I:\Deal-Middle\\Magazine"

# 配置数据
foldername = "第一批数据"
PDFDIR = RESULTDIR + "\\" + foldername + "\\"
PRODUCTDIR = "I:\\Deal-Middle" + "\\ExtractMagazinePDF\\" + foldername + "\\"


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))


def genfile(srcfile, desfile, startpage, endpage):
    """
    根据startpage跟endpage做pdf文件切分
    :param srcfile:
    :param desfile:
    :param startpage:
    :param endpage:
    :return:
    """
    output = PdfFileWriter()
    src = PdfFileReader(file(srcfile, "rb"))
    (filepath, filename) = os.path.split(desfile)
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    des = file(desfile, "wb")
    for i in range(startpage - 1, endpage):
        output.addPage(src.getPage(i))
    output.write(des)
    des.close()
    del src
    del des


def gen_files(logname):
    """
    读取log日志:格式为：文件名 目录名 开始页码 结束页码 文件GUID 目录GUID
    :param logname:
    :return:
    """
    with open(logname, "r") as f1:
        regex_tab = re.compile("\\t")
        regex_line = re.compile("-")
        # 配置数据，读取上一次的最大值
        while True:
            line = f1.readline().decode("utf-8")
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            pageinfo = regex_line.split(info[2])
            startpage = pageinfo[0]
            endpage = pageinfo[1]
            year_month = info[0][-6:]
            if info[0].endswith("201019-20"):
                year_month = info[0][-9:]
            year = year_month[0:4]
            cat_name = info[0][:info[0].rfind(year_month)]
            # print cat_name,year,year_month
            # 切分数据
            genfile((PDFDIR + (info[0])).decode("utf-8").encode("gbk") + '.pdf',
                    PRODUCTDIR + cat_name + "\\" + year + "\\" + year_month + "\\" + info[1]
                    + '.pdf',
                    int(startpage), int(endpage))
            print info[0] + " Gernerate Success..."



def extract_files():
    """
    拆分数据
    :return:
    """
    # 配置数据
    gen_files("MagazinePageOffset.txt")


def main():
    extract_files()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()