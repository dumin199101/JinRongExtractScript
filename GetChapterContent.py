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
    return fstr


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))


def get_book_content(file):

    (filepath, name) = os.path.split(file)
    dirname = filepath
    end_index = dirname.rfind('\\')
    bookname = dirname[end_index + 1:]

    soup = BeautifulSoup(open(file.encode("gbk")), features='xml')

    # 以chapter开头
    chapter = soup.select('chapter')
    # 以bibliography开头
    bibliography = soup.select('bibliography')
    # 以preface开头
    preface = soup.select('preface')
    # 以colophon开头
    colophon = soup.select('colophon')
    # 以dedication开头
    dedication = soup.select('dedication')

    if len(chapter) > 0:
        # 从info标签中获取基本信息
        title = soup.select('chapter > info > title')[0].string
        if title is None:
            for string in soup.title.strings:
                title = string
                break
        pdfpage = soup.select('chapter > info > pagenums[role="pdfpage"]')[0].string
        bookpage = soup.select('chapter > info > pagenums[role="bookpage"]')[0].string
    elif len(bibliography) > 0:
        # 从info标签中获取基本信息
        title = soup.select('bibliography > blockquote > info > title')[0].string
        pdfpage = soup.select('bibliography > blockquote > info > pagenums[role="pdfpage"]')[0].string
        bookpage = soup.select('bibliography > blockquote > info > pagenums[role="bookpage"]')[0].string
    elif len(preface) > 0:
        # 从info标签中获取基本信息
        title = soup.select('preface > info > title')[0].string
        pdfpage = soup.select('preface > info > pagenums[role="pdfpage"]')[0].string
        bookpage = soup.select('preface > info > pagenums[role="bookpage"]')[0].string
    elif len(colophon) > 0:
        # 从info标签中获取基本信息
        title = soup.select('colophon > info > title')[0].string
        pdfpage = soup.select('colophon > info > pagenums[role="pdfpage"]')[0].string
        bookpage = soup.select('colophon > info > pagenums[role="bookpage"]')[0].string
    elif len(dedication) > 0:
        # 从info标签中获取基本信息
        title = soup.select('dedication > info > title')[0].string
        if title is None:
            for string in soup.title.strings:
                title = string
                break
        pdfpage = soup.select('dedication > info > pagenums[role="pdfpage"]')[0].string
        bookpage = soup.select('dedication > info > pagenums[role="bookpage"]')[0].string

    """
    获取正文内容：
    将所有info标签中的数据去掉
    for tag in soup.chapter.info.next_siblings:
        if tag.name is not None:
            print tag.name
    """
    # 声明一个集合统计标签种类：创建空集合必须使用set函数，非空集合可以使用{}
    tag_set = set()
    for tag in soup.find_all(True):
        tag_set.add(tag.name)
    print "*" * 100
    # 查询所有标签做分析
    for tag in tag_set:
        print "此文档中存在的标签：", tag
    print "*" * 100
    # 等统计完所有的再动态添加，这里只统计单级标签
    tag_allow_set = {'title', 'para'}
    info = ''
    for tag in soup.find_all(True):
        if tag.parent.name == 'info':
            continue
        if tag.parent.name == 'footnote':
            continue
        if tag.parent.name == 'textobject':
            continue
        if tag.parent.name == 'annotation':
            continue
        if tag.name in tag_allow_set:
            if tag.string is not None:
                info = info + tag.string
                # print tag.string
            else:
                if tag.name == 'para':
                    for string in tag.strings:
                        if str(string).isdigit():
                            continue
                        info = info + string
                        # print string
    # print bookname + "\t" + title + "\t" + pdfpage + "\t" + bookpage + "\t" + del_blank_char(info)
    info = bookname + "\t"  + title + "\t" + pdfpage + "\t" + bookpage + "\t" + del_blank_char(info) + "\n"
    write_mapping_log("Check_Content_File_1.txt",info)
    print title + " Get Content Successfully..."


def get_all_book_content(srcdir):
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir, filename)
        if os.path.isdir(file):
            get_all_book_content(file)
        else:
            if filename.endswith("xml"):
                get_book_content(file)



def main():
    # 配置数据
    srcdir = u"E:\Goosuu\JinRong\Script\Deal-Middle\Chapter_XML\第一批数据"
    get_all_book_content(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
