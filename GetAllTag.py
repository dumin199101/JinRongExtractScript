# coding=utf-8
import os
import sys
from bs4 import BeautifulSoup
import re

ROOTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))


def del_blank_char(str):
    """
    去除字符串中的空白跟换行符
    :param str:
    :return:
    """
    rep = re.compile(r'(\n|\t|\r)')
    (fstr, count) = rep.subn('', str)
    return fstr.replace(" ", "")


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))


def get_all_tag(srcdir):
    global tag_set
    tag_set = {}
    # tag_set = set()
    get_tags(srcdir,tag_set)
    print "*" * 100
    # 查询所有标签做分析
    for key,tag in tag_set.items():
        print key, tag
    # for tag in tag_set:
    #     print tag
    print "*" * 100


def get_tags(srcdir,tag_set):
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir, filename)
        if os.path.isdir(file):
            get_tags(file,tag_set)
        else:
            (filepath, name) = os.path.split(file)
            dirname = filepath
            end_index = dirname.rfind('\\')
            bookname = dirname[end_index + 1:]
            if filename.endswith("xml"):
                soup = BeautifulSoup(open(file.encode('gbk')), features='xml')
                for tag in soup.find_all(True):
                    tag_set[tag.name] = bookname + ":" + name
                    # tag_set.add(tag.name)
        print file + " Get Tag success"

def main():
    # 配置数据
    # srcdir = u"E:\Goosuu\JinRong\Script\Deal-Middle\Chapter_XML\第一批数据"
    # srcdir = u"E:\Goosuu\JinRong\Script\Deal-Middle\Chapter_XML\第二批数据"
    # srcdir = u"E:\Goosuu\JinRong\Script\Deal-Middle\Chapter_XML\第三批数据"
    srcdir = u"I:\\Deal-Middle\\EXTRACTCDATAXML"
    get_all_tag(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
