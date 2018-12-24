# coding=utf-8
"""
@Project: JinRong
@Time: 2018/12/24 16:11
@Name: ExtractMagazineCData
@Author: lieyan123091
"""
import sys
import os

ROOTDIR = "I:\\Deal-Middle"
RESULTDIR = ROOTDIR + "\\EXTRACTCDATAXML\\"


def write_xml(name, content):
    """
    重新写入XML文件
    :return:
    """
    with open(name, "w") as f1:
        f1.write(content.encode("utf-8"))

def read_xml(name):
    """
    读取XML文件内容
    :param name:
    :return:
    """
    with open(name,"r") as f1:
        return f1.read().replace("<![CDATA[","").replace("]]>","")



def extract_magazine_cdata(srcdir):
    for filename in os.listdir(srcdir):
        if not os.path.exists(RESULTDIR):
            os.makedirs(RESULTDIR)
        content = read_xml(srcdir+"\\"+filename)
        destfile = RESULTDIR + filename
        write_xml(destfile,content)
        print filename + " Get Content ..."



def main():
    srcdir = u"I:\\Deal-Middle\\MagazineXML\\第一批数据"
    extract_magazine_cdata(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()