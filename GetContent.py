# coding=utf-8

import os
import sys
from bs4 import BeautifulSoup
import re



ROOTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))


def remove_blank_char(s):
    """
    去除空白字符
    :param s:
    :return:
    """
    return ''.join(s.split())


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
    """
    获取所有层级标题&正文
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
    print "*" * 100
    # 查询所有标签做分析
    for tag in tag_set:
        print "此文档中存在的标签：", tag
    print "*" * 100

    title = None
    part_title = None

    # 获取正文内容：
    def get_part_chapter_content():
        """
            （1）一级part标签正文
            :return:
            """
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
        # print part_title + "\t" + pdfpage + "\t" + bookpage + "\t" + del_blank_char(info)
        info = bookname + "\t" + part_title + "\t" + level[
                                                      7:] + "\t" + pdfpage + "\t" + bookpage + "\t" + bookname + "_" + level[
                                                                                                                       7:] + "_" + part_title + "\t" + del_blank_char(
            info) + "\n"
        write_mapping_log("Check_Content_File.txt",info)
        print bookname + "\t" +part_title + " Get Content Successfully..."

    def get_chapters_content(chapt):
        """
        （1）二级标签chapter正文,多个chapters
         :return:
        """
        # 等统计完所有的再动态添加，这里只统计单级标签
        tag_allow_set = {'title', 'para'}
        info = ''
        for tag in chapt.find_all(True):
            if tag.parent.name == 'info':
                continue
            if tag.parent.name == 'footnote':
                continue
            if tag.parent.name == 'textobject':
                continue
            if tag.parent.name == 'annotation':
                continue
            if tag.parent.name == 'partintro':
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
        # print chapt_title + "\t" + chapt_pdfpage + "\t" + chapt_bookpage + "\t" + del_blank_char(info)
        info =  bookname + "\t" + chapt_title + "\t" + chapt_level[
                                                7:] + "\t" +chapt_pdfpage + "\t" + chapt_bookpage + "\t" + bookname + "_" + chapt_level[
                                                                                                                 7:] + "_" + chapt_title + "\t" + del_blank_char(
            info) + "\n"
        write_mapping_log("Check_Content_File.txt",info)
        print bookname + "_" +chapt_title + " Get Content Successfully..."





    def get_chapter_content():
        """
        （1）一级标签正文
        :return:
        """
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
            if tag.parent.name == 'partintro':
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
        # print bookname + "\t" + title + "\t" + level[
        #                                        7:] + "\t" + pdfpage + "\t" + bookpage + "\t" + bookname + "_" + level[
        #                                                                                                         7:] + "_" + title + "\t" + del_blank_char(
        #     info)
        info = bookname + "\t" + title + "\t" + level[
                                                7:] + "\t" + pdfpage + "\t" + bookpage + "\t" + bookname + "_" + level[
                                                                                                                 7:] + "_" + title + "\t" + del_blank_char(
            info) + "\n"
        write_mapping_log("Check_Content_File.txt", info)
        print bookname + "_" + title + " Get Content Successfully..."

    def get_sect1_content(xmlid):
        """
        获取二级标签正文内容:利用标签跟xmlid进行唯一定位
        :return:
        """
        tag_allow_set = {'title', 'para'}
        sect1_info = ''
        # 先定位当前sect1标签
        sect1_title_tag = soup.find(attrs={"xml:id": xmlid})
        sect1_tag = sect1_title_tag.parent
        for tag in sect1_tag.descendants:
            if tag.name is not None:
                if tag.parent.name == 'info':
                    continue
                if tag.parent.name == 'footnote':
                    continue
                if tag.parent.name == 'textobject':
                    continue
                if tag.parent.name == 'annotation':
                    continue
                if tag.parent.name == 'partintro':
                    continue
                if tag.name in tag_allow_set:
                    if tag.string is not None:
                        sect1_info = sect1_info + tag.string
                        # print tag.string
                    else:
                        if tag.name == 'para':
                            for string in tag.strings:
                                if str(string).isdigit():
                                    continue
                                sect1_info = sect1_info + string
                                # print string
        # print bookname + "\t" + sect1_title + "\t" + sect1_level[
        #                                              7:] + "\t" + sect1_pdfpage + "\t" + sect1_bookpage + "\t" + bookname + "_" + sect1_level[
        #                                                                                                                           7:] + "_" + sect1_title + "\t" + del_blank_char(
        #     sect1_info)
        sect1_info = bookname + "\t" + sect1_title + "\t" + sect1_level[
                                                            7:] + "\t" + sect1_pdfpage + "\t" + sect1_bookpage + "\t" + bookname + "_" + sect1_level[
                                                                                                                                         7:] + "_" + sect1_title + "\t" + del_blank_char(
            sect1_info) + "\n"
        write_mapping_log("Check_Content_File.txt", sect1_info)
        print bookname + "_" + sect1_title + " Get Content Successfully..."

    def get_sect2_content(xmlid):
        """
        获取三级标签正文内容
        :return:
        """
        tag_allow_set = {'title', 'para'}
        sect2_info = ''
        # 先定位当前sect1标签
        sect2_title_tag = soup.find(attrs={"xml:id": xmlid})
        sect2_tag = sect2_title_tag.parent
        for tag in sect2_tag.descendants:
            if tag.name is not None:
                if tag.parent.name == 'info':
                    continue
                if tag.parent.name == 'footnote':
                    continue
                if tag.parent.name == 'textobject':
                    continue
                if tag.parent.name == 'annotation':
                    continue
                if tag.parent.name == 'partintro':
                    continue
                if tag.name in tag_allow_set:
                    if tag.string is not None:
                        sect2_info = sect2_info + tag.string
                        # print tag.string
                    else:
                        if tag.name == 'para':
                            for string in tag.strings:
                                if str(string).isdigit():
                                    continue
                                sect2_info = sect2_info + string
                                # print string
        # print bookname + "\t" + sect2_title + "\t" + sect2_level[
        #                                              7:] + "\t" + sect2_pdfpage + "\t" + sect2_bookpage + "\t" + bookname + "_" + sect2_level[
        #                                                                                                                           7:] + "_" + sect2_title + "\t" + del_blank_char(
        #     sect2_info)

        sect2_info = bookname + "\t" + sect2_title + "\t" + sect2_level[
                                                            7:] + "\t" + sect2_pdfpage + "\t" + sect2_bookpage + "\t" + bookname + "_" + sect2_level[
                                                                                                                                         7:] + "_" + sect2_title + "\t" + del_blank_char(
            sect2_info) + "\n"
        write_mapping_log("Check_Content_File.txt", sect2_info)
        print bookname + "_" + sect2_title + " Get Content Successfully..."

    def get_sect3_content(xmlid):
        """
        获取四级标签正文内容
        :return:
        """
        tag_allow_set = {'title', 'para'}
        sect3_info = ''
        # 先定位当前sect1标签
        sect3_title_tag = soup.find(attrs={"xml:id": xmlid})
        sect3_tag = sect3_title_tag.parent
        for tag in sect3_tag.descendants:
            if tag.name is not None:
                if tag.parent.name == 'info':
                    continue
                if tag.parent.name == 'footnote':
                    continue
                if tag.parent.name == 'textobject':
                    continue
                if tag.parent.name == 'annotation':
                    continue
                if tag.parent.name == 'partintro':
                    continue
                if tag.name in tag_allow_set:
                    if tag.string is not None:
                        sect3_info = sect3_info + tag.string
                        # print tag.string
                    else:
                        if tag.name == 'para':
                            for string in tag.strings:
                                if str(string).isdigit():
                                    continue
                                sect3_info = sect3_info + string
                                # print string
        # print bookname + "\t" + sect3_title + "\t" + sect3_level[
        #                                              7:] + "\t" + sect3_pdfpage + "\t" + sect3_bookpage + "\t" + bookname + "_" + sect3_level[
        #                                                                                                                           7:] + "_" + sect3_title + "\t" + del_blank_char(
        #     sect3_info)

        sect3_info = bookname + "\t" + sect3_title + "\t" + sect3_level[
                                                            7:] + "\t" + sect3_pdfpage + "\t" + sect3_bookpage + "\t" + bookname + "_" + sect3_level[
                                                                                                                                         7:] + "_" + sect3_title + "\t" + del_blank_char(
            sect3_info) + "\n"
        write_mapping_log("Check_Content_File.txt", sect3_info)
        print bookname + "_" + sect3_title + " Get Content Successfully..."

    def get_sect4_content(xmlid):
        """
        获取五级标签正文内容
        :return:
        """
        tag_allow_set = {'title', 'para'}
        sect4_info = ''
        # 先定位当前sect1标签
        sect4_title_tag = soup.find(attrs={"xml:id": xmlid})
        sect4_tag = sect4_title_tag.parent
        for tag in sect4_tag.descendants:
            if tag.name is not None:
                if tag.parent.name == 'info':
                    continue
                if tag.parent.name == 'footnote':
                    continue
                if tag.parent.name == 'textobject':
                    continue
                if tag.parent.name == 'annotation':
                    continue
                if tag.parent.name == 'partintro':
                    continue
                if tag.name in tag_allow_set:
                    if tag.string is not None:
                        sect4_info = sect4_info + tag.string
                        # print tag.string
                    else:
                        if tag.name == 'para':
                            for string in tag.strings:
                                if str(string).isdigit():
                                    continue
                                sect4_info = sect4_info + string
                                # print string
        # print bookname + "\t" + sect4_title + "\t" + sect4_level[
        #                                              7:] + "\t" + sect4_pdfpage + "\t" + sect4_bookpage + "\t" + bookname + "_" + sect4_level[
        #                                                                                                                           7:] + "_" + sect4_title + "\t" + del_blank_char(
        #     sect4_info)

        sect4_info = bookname + "\t" + sect4_title + "\t" + sect4_level[
                                                            7:] + "\t" + sect4_pdfpage + "\t" + sect4_bookpage + "\t" + bookname + "_" + sect4_level[
                                                                                                                                         7:] + "_" + sect4_title + "\t" + del_blank_char(
            sect4_info) + "\n"
        write_mapping_log("Check_Content_File.txt", sect4_info)
        print bookname + "_" + sect4_title + " Get Content Successfully..."

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
        bookpage = chapt.select('info > pagenums[role="bookpage"]')[0].string
        return (level, title, pdfpage, bookpage)

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
        bookpage = soup.select('part > info > pagenums[role="bookpage"]')[0].string



    # 统计一级标签part信息，包含多个chapter
    if part_title is not None:
        # print level, level[7:], part_title, pdfpage, bookpage
        get_part_chapter_content()

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
        bookpage = soup.select('chapter > info > pagenums[role="bookpage"]')[0].string
    elif len(chapter) > 1:
        chapters = soup.select('chapter')
        for chapt in chapters:
            (chapt_level, chapt_title, chapt_pdfpage, chapt_bookpage) = get_chapt_info(chapt)
            if chapt_title is not None:
                # print chapt_level, chapt_level[7:], chapt_title, chapt_pdfpage, chapt_bookpage
                get_chapters_content(chapt)
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
        bookpage = soup.select('bibliography > blockquote > info > pagenums[role="bookpage"]')[0].string
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
        bookpage = soup.select('preface > info > pagenums[role="bookpage"]')[0].string
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
        bookpage = soup.select('colophon > info > pagenums[role="bookpage"]')[0].string
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
        bookpage = soup.select('dedication > info > pagenums[role="bookpage"]')[0].string
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
        bookpage = soup.select('index > info > pagenums[role="bookpage"]')[0].string
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
        bookpage = soup.select('appendix > info > pagenums[role="bookpage"]')[0].string

    # print title,pdfpage,bookpage
    # 统计一级标签信息
    if title is not None:
        # print level, level[7:], title, pdfpage, bookpage
        get_chapter_content()

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
            sect1_bookpage = sect1.select('info > pagenums[role="bookpage"]')[0].string

            # 统计二级标签信息(存在多个)
            # print sect1_level, sect1_level[7:], sect1_title, sect1_bookpage, sect1_pdfpage
            get_sect1_content(xmlid)

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
            sect2_bookpage = sect2.select('info > pagenums[role="bookpage"]')[0].string

            # 统计三级标签信息
            # print sect2_level, sect2_level[7:], sect2_title, sect2_bookpage, sect2_pdfpage
            get_sect2_content(xmlid)

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
            sect3_bookpage = sect3.select('info > pagenums[role="bookpage"]')[0].string

            # 统计四级标签信息
            # print sect3_level, sect3_level[7:], sect3_title, sect3_bookpage, sect3_pdfpage
            get_sect3_content(xmlid)

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
            sect4_bookpage = sect4.select('info > pagenums[role="bookpage"]')[0].string

            # 统计五级标签信息
            # print sect4_level, sect4_level[7:], sect4_title, sect4_bookpage, sect4_pdfpage
            get_sect4_content(xmlid)


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
    # srcdir = u"E:\Goosuu\JinRong\Script\Deal-Middle\Chapter_XML\第一批数据"
    # srcdir = u"E:\Goosuu\JinRong\Script\Deal-Middle\Chapter_XML\第二批数据"
    srcdir = u"E:\Goosuu\JinRong\Script\Deal-Middle\Chapter_XML\第三批数据"
    get_all_book_content(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
