# coding=utf-8
import os
import sys
import re

ROOTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))
SCRIPTDIR = "E:\\Goosuu\\JinRong\\Script"
XPDFDIR =  SCRIPTDIR + '\\xpdf'
RESULTDIR = SCRIPTDIR + "\\Result"

# 配置数据
PDFDIR = RESULTDIR + "\\第一批数据\\"


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))

def GetPdfpages(filename):
    """
    获取PDF文件的页码数
    :param filename:
    :return:
    """
    infofile = sys.argv[0][0:sys.argv[0].rfind('\\') + 1] + 'info.txt'
    os.chdir(XPDFDIR)
    os.system('pdfinfo.exe -box \"' + filename + '\" >\"' + infofile + '\"')
    fp = open(infofile, 'r+')
    while True:
        tempstr = fp.readline()
        if tempstr.find('Pages') > -1:
            pages = int(tempstr[tempstr.index(':') + 1:].strip())
            break
    fp.close()
    os.system("del " + infofile)
    os.chdir(ROOTDIR)
    return pages


def extract_chapter(txtpath):
    """
    读取log日志
    :param txtpath:
    :return:
    """
    rep = re.compile(r'\t')
    mapping_file = open(txtpath, "r")
    line_1st = mapping_file.readline()
    while True:
        # 根据读取下一行的长度，判断循环结束条件
        if len(line_1st) < 1:
            break
        line_2nd = mapping_file.readline()
        (fields1st) = rep.split(line_1st)
        startpage = int(fields1st[4])
        if len(line_2nd) < 1:
            # 说明到达最后一行
            endpage = GetPdfpages((PDFDIR + (fields1st[1])).encode("gbk") + ".pdf")
        else:
            (fields2nd) = rep.split(line_2nd)
            endpage = int(fields2nd[4]) - 1
        if endpage < startpage:
            # 多本书同时拆分的情况:到达单本书的末尾
            endpage = GetPdfpages((PDFDIR + (fields1st[1])).encode("gbk") + ".pdf")
        line_1st = line_2nd
        # print fields1st[1] + "_" + fields1st[0] + "\t" + str(startpage) + "-" + str(endpage)
        info = fields1st[0] + "\t" + fields1st[1] + "\t" + str(startpage) + "\t" + str(endpage) + "\n"
        write_mapping_log("Chapter_Page_Offset_File.txt",info)
        print fields1st[1] + "_" + fields1st[0] + " Compute Success..."


def get_page_offset():
    """
    计算页码偏移
    :return:
    """
    # 配置数据
    extract_chapter("Chapter_File.txt")



def main():
  get_page_offset()



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()