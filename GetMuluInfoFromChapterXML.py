# coding=utf-8
"""
@Project: JinRong
@Time: 2018/10/11 10:42
@Name: GetMuluInfoFromChapterXML
@Author: lieyan123091
"""

import os
import sys
from bs4 import BeautifulSoup




ROOTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))

def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))


def get_title_info(file):
    """
    获取所有层级标题
    :return:
    """
    (filepath, name) = os.path.split(file)
    dirname = filepath
    end_index = dirname.rfind('\\')
    bookname = dirname[end_index + 1:]

    soup = BeautifulSoup(open(file.encode("gbk")), features='xml')

    # 声明一个集合统计标签种类：创建空集合必须使用set函数，非空集合可以使用{}
    tag_set = set()
    for tag in soup.find_all(True):
        tag_set.add(tag.name)


    title = None
    part_title = None


    def get_chapt_info(chapt):
        level = chapt.find('title').get('xml:id')
        if level.rfind(".") > -1:
            level = level[:level.rfind(".")]
        title = chapt.select('info > title')[0].string
        if title is None:
            for string in chapt.title.strings:
                title = string
                break
        pdfpage = chapt.select('info > pagenums[role="pdfpage"]')[0].string
        return (level, title, pdfpage)

    # 处理一级标签

    # 以part开头
    part = soup.select('part')

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
    # 以index开头
    index = soup.select('index')
    # 以appendix开头
    appendix = soup.select('appendix')

    # part中包含chapter
    if len(part) > 0:
        # 从info标签中获取基本信息
        level = part[0].find('title').get('xml:id')
        if level.rfind(".") > -1:
            level = level[:level.rfind(".")]
        part_title = soup.select('part > info > title')[0].string
        # 这种情况是处理title标签中有多个标签的情况
        if part_title is None:
            for string in soup.title.strings:
                part_title = string
                break
        pdfpage = soup.select('part > info > pagenums[role="pdfpage"]')[0].string




    # 统计一级标签part信息，包含多个chapter
    if part_title is not None:
        # 统计目录层级
        count = level.count("-")
        # print part_title,bookname,name+"#"+level,name,level, level[7:],str(count+1),pdfpage
        strs = part_title+"\t"+bookname+"\t"+name+"#"+level+"\t"+name+"\t"+level+"\t"+level[7:]+"\t"+str(count+1)+"\t"+pdfpage + "\n"
        write_mapping_log("parseMuluXMLFromChapterXML.txt",strs)
        print bookname + "_" + part_title



    if len(chapter) == 1:
        # 从info标签中获取基本信息
        level = chapter[0].find('title').get('xml:id')
        if level.rfind(".") > -1:
            level = level[:level.rfind(".")]
        title = soup.select('chapter > info > title')[0].string
        if title is None:
            for string in soup.title.strings:
                title = string
                break
        pdfpage = soup.select('chapter > info > pagenums[role="pdfpage"]')[0].string

    elif len(chapter) > 1:
        chapters = soup.select('chapter')
        for chapt in chapters:
            (chapt_level, chapt_title, chapt_pdfpage) = get_chapt_info(chapt)
            # 统计目录层级
            count = chapt_level.count("-")
            # print chapt_title, bookname, name + "#" + chapt_level, name, chapt_level, chapt_level[7:], str(count + 1), chapt_pdfpage
            strs = chapt_title + "\t" + bookname + "\t" + name + "#" + chapt_level + "\t" + name + "\t" + chapt_level + "\t" + chapt_level[7:] + "\t" + str(count + 1) + "\t" + chapt_pdfpage + "\n"
            write_mapping_log("parseMuluXMLFromChapterXML.txt", strs)
            print bookname + "_" + chapt_title
    elif len(bibliography) > 0:
        # 从info标签中获取基本信息
        level = bibliography[0].blockquote.find('title').get('xml:id')
        if level.rfind(".") > -1:
            level = level[:level.rfind(".")]
        title = soup.select('bibliography > blockquote > info > title')[0].string
        if title is None:
            for string in soup.title.strings:
                title = string
                break
        pdfpage = soup.select('bibliography > blockquote > info > pagenums[role="pdfpage"]')[0].string

    elif len(preface) > 0:
        # 从info标签中获取基本信息
        level = preface[0].find('title').get('xml:id')
        if level.rfind(".") > -1:
            level = level[:level.rfind(".")]
        title = soup.select('preface > info > title')[0].string
        if title is None:
            for string in soup.title.strings:
                title = string
                break
        pdfpage = soup.select('preface > info > pagenums[role="pdfpage"]')[0].string

    elif len(colophon) > 0:
        # 从info标签中获取基本信息
        level = colophon[0].find('title').get('xml:id')
        if level.rfind(".") > -1:
            level = level[:level.rfind(".")]
        title = soup.select('colophon > info > title')[0].string
        if title is None:
            for string in soup.title.strings:
                title = string
                break
        pdfpage = soup.select('colophon > info > pagenums[role="pdfpage"]')[0].string

    elif len(dedication) > 0:
        # 从info标签中获取基本信息
        level = dedication[0].find('title').get('xml:id')
        if level.rfind(".") > -1:
            level = level[:level.rfind(".")]
        title = soup.select('dedication > info > title')[0].string
        # 这种情况是处理title标签中有多个标签的情况
        if title is None:
            for string in soup.title.strings:
                title = string
                break
        pdfpage = soup.select('dedication > info > pagenums[role="pdfpage"]')[0].string

    elif len(index) > 0:
        # 从info标签中获取基本信息
        level = index[0].find('title').get('xml:id')
        if level.rfind(".") > -1:
            level = level[:level.rfind(".")]
        title = soup.select('index > info > title')[0].string
        # 这种情况是处理title标签中有多个标签的情况
        if title is None:
            for string in soup.title.strings:
                title = string
                break
        pdfpage = soup.select('index > info > pagenums[role="pdfpage"]')[0].string

    elif len(appendix) > 0:
        # 从info标签中获取基本信息
        level = appendix[0].find('title').get('xml:id')
        if level.rfind(".") > -1:
            level = level[:level.rfind(".")]
        title = soup.select('appendix > info > title')[0].string
        # 这种情况是处理title标签中有多个标签的情况
        if title is None:
            for string in soup.title.strings:
                title = string
                break
        pdfpage = soup.select('appendix > info > pagenums[role="pdfpage"]')[0].string


    if title is not None:
        # 统计目录层级
        count = level.count("-")
        # print title, bookname, name + "#" + level, name, level, level[7:], str(count + 1), pdfpage
        strs = title + "\t" + bookname + "\t" + name + "#" + level + "\t" + name + "\t" + level + "\t" + level[7:] + "\t" + (str(int(count+1))) + "\t" +  pdfpage + "\n"
        write_mapping_log("parseMuluXMLFromChapterXML.txt", strs)
        print bookname + "_" + title


    # 处理二级标签、三级标签、四级标签
    if 'sect1' in tag_set:
        sect1s = soup.select('sect1')
        for sect1 in sect1s:
            xmlid = sect1.find('title').get('xml:id')
            if xmlid.rfind(".") > -1:
                sect1_level = xmlid[:xmlid.rfind(".")]
            else:
                sect1_level = xmlid
            sect1_title = sect1.select('info > title')[0].string
            if sect1_title is None:
                for string in sect1.select('info > title')[0].strings:
                    sect1_title = string
                    break
            sect1_pdfpage = sect1.select('info > pagenums[role="pdfpage"]')[0].string
            # 统计目录层级
            count = sect1_level.count("-")
            # print sect1_title, bookname, name + "#" + sect1_level, name, sect1_level, sect1_level[7:], str(
            #     count + 1), sect1_pdfpage
            strs = sect1_title + "\t" + bookname + "\t" + name + "#" + sect1_level + "\t" + name + "\t" + sect1_level + "\t" + sect1_level[
                                                                                                             7:] + "\t" + str(
                count + 1) + "\t" + sect1_pdfpage + "\n"
            write_mapping_log("parseMuluXMLFromChapterXML.txt", strs)
            print bookname + "_" + sect1_title





    if 'sect2' in tag_set:
        sect2s = soup.select('sect2')
        for sect2 in sect2s:
            xmlid = sect2.find('title').get('xml:id')
            if xmlid.rfind(".") > -1:
                sect2_level = xmlid[:xmlid.rfind(".")]
            else:
                sect2_level = xmlid
            sect2_title = sect2.select('info > title')[0].string
            if sect2_title is None:
                for string in sect2.select('info > title')[0].strings:
                    sect2_title = string
                    break
            sect2_pdfpage = sect2.select('info > pagenums[role="pdfpage"]')[0].string
            # 统计目录层级
            count = sect2_level.count("-")
            # print sect2_title, bookname, name + "#" + sect2_level, name, sect2_level, sect2_level[7:], str(
            #     count + 1), sect2_pdfpage
            strs = sect2_title + "\t" + bookname + "\t" + name + "#" + sect2_level + "\t" + name + "\t" + sect2_level + "\t" + sect2_level[
                                                                                                                               7:] + "\t" + str(
                count + 1) + "\t" + sect2_pdfpage + "\n"
            write_mapping_log("parseMuluXMLFromChapterXML.txt", strs)
            print bookname + "_" + sect2_title



    if 'sect3' in tag_set:
        sect3s = soup.select('sect3')
        for sect3 in sect3s:
            xmlid = sect3.find('title').get('xml:id')
            if xmlid.rfind(".") > -1:
                sect3_level = xmlid[:xmlid.rfind(".")]
            else:
                sect3_level = xmlid
            sect3_title = sect3.select('info > title')[0].string
            if sect3_title is None:
                for string in sect3.select('info > title')[0].strings:
                    sect3_title = string
                    break
            sect3_pdfpage = sect3.select('info > pagenums[role="pdfpage"]')[0].string
            # 统计目录层级
            count = sect3_level.count("-")
            # print sect3_title, bookname, name + "#" + sect3_level, name, sect3_level, sect3_level[7:], str(
            #     count + 1), sect3_pdfpage
            strs = sect3_title + "\t" + bookname + "\t" + name + "#" + sect3_level + "\t" + name + "\t" + sect3_level + "\t" + sect3_level[
                                                                                                                               7:] + "\t" + str(
                count + 1) + "\t" + sect3_pdfpage + "\n"
            write_mapping_log("parseMuluXMLFromChapterXML.txt", strs)
            print bookname + "_" + sect3_title




    if 'sect4' in tag_set:
        sect4s = soup.select('sect4')
        for sect4 in sect4s:
            xmlid = sect4.find('title').get('xml:id')
            if xmlid.rfind(".") > -1:
                sect4_level = xmlid[:xmlid.rfind(".")]
            else:
                sect4_level = xmlid
            sect4_title = sect4.select('info > title')[0].string
            if sect4_title is None:
                for string in sect4.select('info > title')[0].strings:
                    sect4_title = string
                    break
            sect4_pdfpage = sect4.select('info > pagenums[role="pdfpage"]')[0].string
            # 统计目录层级
            count = sect4_level.count("-")
            # print sect4_title, bookname, name + "#" + sect4_level, name, sect4_level, sect4_level[7:], str(
            #     count + 1), sect4_pdfpage
            strs = sect4_title + "\t" + bookname + "\t" + name + "#" + sect4_level + "\t" + name + "\t" + sect4_level + "\t" + sect4_level[
                                                                                                                               7:] + "\t" + str(
                count + 1) + "\t" + sect4_pdfpage + "\n"
            write_mapping_log("parseMuluXMLFromChapterXML.txt", strs)
            print bookname + "_" + sect4_title




def get_muluinfo_from_chapterxml(srcdir):
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir, filename)
        if os.path.isdir(file):
            get_muluinfo_from_chapterxml(file)
        else:
            if filename.endswith("xml"):
                get_title_info(file)


def main():
    # 配置数据
    srcdir = u"E:\Goosuu\JinRong\Script\Deal-Middle\Chapter_XML\第二批数据"
    get_muluinfo_from_chapterxml(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()

