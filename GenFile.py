# coding=utf-8
import os
import sys
import re
from pyPdf import PdfFileWriter, PdfFileReader

ROOTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))
SCRIPTDIR = "E:\\Goosuu\\JinRong\\Script"
RESULTDIR = SCRIPTDIR + "\\Result"

# 配置数据
foldername = "第一批数据"
PDFDIR = RESULTDIR + "\\" + foldername + "\\"
PRODUCTDIR = SCRIPTDIR + "\\Product\\" + foldername + "\\"


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

"""
def gen_files(logname):
    with open(logname, "r") as f1:
        regex_tab = re.compile("\\t")
        # 配置数据，读取上一次的最大值
        i = 1
        while True:
            line = f1.readline().decode("utf-8")
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            newname = info[0].replace(":", "").replace("/", "").replace("‐", "")
            name = str(i) + "_" + newname
            string = str(i) + "\t" + info[0] + "\t" + info[1] + "\t" + info[1] + "_" + info[
                0] + "\t" + newname + "\t" + name + "\n"
            write_mapping_log("RenameRefer.txt", string)
            # 切分数据
            genfile((PDFDIR + (info[1])).decode("utf-8").encode("gbk") + '.pdf',
                    (PRODUCTDIR + info[1] + "\\" + (
                    str(i) + "_" + info[0].replace(":", "").replace("/", "").replace("‐", ""))).encode(
                        "gbk") + '.pdf',
                    int(info[2]), int(info[3]))
            print name + " Gernerate Success..."
            i = i + 1
"""


def gen_files(logname):
    """
    读取log日志:格式为：文件名 目录名 开始页码 结束页码 文件GUID 目录GUID
    :param logname:
    :return:
    """
    with open(logname, "r") as f1:
        regex_tab = re.compile("\\t")
        # 配置数据，读取上一次的最大值
        while True:
            line = f1.readline().decode("utf-8")
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            # 切分数据
            genfile((PDFDIR + (info[1])).decode("utf-8").encode("gbk") + '.pdf',
                    PRODUCTDIR + info[5] + "\\" + info[4]
                    + '.pdf',
                    int(info[2]), int(info[3]))
            print info[0] + " Gernerate Success..."



def extract_files():
    """
    拆分数据
    :return:
    """
    # 配置数据
    gen_files("Page_Offset_File.txt")


def main():
    extract_files()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
