# coding=utf-8
"""
@Project: JinRong
@Time: 2018/12/29 16:36
@Name: GetMagazineContent
@Author: lieyan123091
"""
import sys
import os
from bs4 import BeautifulSoup
import re

def del_blank_char(str):
    """
    去除字符串中的空白跟换行符
    :param str:
    :return:
    """
    rep = re.compile(r'(\n|\t|\s+)')
    (fstr, count) = rep.subn('', str)
    return fstr

def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))

def get_magazine_content(file):
    (filepath, name) = os.path.split(file)
    (bookname, extension) = os.path.splitext(name)
    soup = BeautifulSoup(open(file.encode("gbk")), features='xml')

    """
    获取正文内容：
    """
    # 声明一个集合统计标签种类：创建空集合必须使用set函数，非空集合可以使用{}
    tag_set = set()
    for tag in soup.find_all(True):
        tag_set.add(tag.name)
    #print "*" * 100
    # 查询所有标签做分析
    # for tag in tag_set:
    #     print "此文档中存在的标签：", tag
    # print "*" * 100
    # 等统计完所有的再动态添加，这里只统计单级标签
    tag_allow_set = {'title', 'para'}
    info = ''
    for tag in soup.find_all(True):
        if tag.parent.name == 'article-info':
            continue
        if tag.parent.name == 'figure':
            continue
        if tag.parent.name == 'info':
            continue
        if tag.name in tag_allow_set:
            if tag.string is not None:
                info = info + tag.string
            else:
                if tag.name == 'para':
                    for string in tag.strings:
                        info = info + string
    write_mapping_log("MagazinePDFContent.txt",bookname+"\t"+del_blank_char(info)+"\n")
    print bookname


def get_magazine_contents(srcdir):
    for filename in os.listdir(srcdir):
        get_magazine_content(os.path.join(srcdir,filename))


def main():
    srcdir = u"I:\\Deal-Middle\\EXTRACTCDATAXML"
    get_magazine_contents(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()