# coding=utf-8
"""
@Project: JinRong
@Time: 2018/10/16 15:20
@Name: GetImageRelateContent
@Author: lieyan123091
获取图片相关正文信息
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


def get_image_relate_content(file):
    """
    获取图片的所有父级标签的集合&获取图片相关的正文信息
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

        # print "*" * 100
        # 查询所有标签做分析
        # for tag in tag_set:
        # print "此文档中存在的标签：", tag

    # print "*" * 100

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
                else:
                    if tag.name == 'para':
                        for string in tag.strings:
                            if str(string).isdigit():
                                continue
                            info = info + string
        # print bookname+"_"+image,bookname,title, cat, image, page, del_blank_char(info)
        info = bookname+"_"+image+"\t"+bookname+"\t"+title+"\t"+cat+"\t"+image+"\t"+page+"\t"+del_blank_char(info) + "\n"
        write_mapping_log("Get_Images_Content.txt", info)
        print bookname,title

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
                else:
                    if tag.name == 'para':
                        for string in tag.strings:
                            if str(string).isdigit():
                                continue
                            info = info + string
        # print bookname+"_"+image,bookname,title, cat, image, page, del_blank_char(info)
        info = bookname+"_"+image+"\t"+bookname + "\t" + title + "\t" + cat + "\t" + image + "\t" + page + "\t" + del_blank_char(info) + "\n"
        write_mapping_log("Get_Images_Content.txt", info)
        print bookname,title

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
                else:
                    if tag.name == 'para':
                        for string in tag.strings:
                            if str(string).isdigit():
                                continue
                            info = info + string
        # print bookname+"_"+image,bookname, title, cat, image, page, del_blank_char(info)
        info = bookname+"_"+image+"\t"+bookname + "\t" + title + "\t" + cat + "\t" + image + "\t" + page + "\t" + del_blank_char(info) + "\n"
        write_mapping_log("Get_Images_Content.txt", info)
        print bookname,title

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
        # print bookname+"_"+image,bookname,title, cat, image, page, del_blank_char(sect1_info)
        sect1_info = bookname+"_"+image+"\t"+bookname + "\t" + title + "\t" + cat + "\t" + image + "\t" + page + "\t" + del_blank_char(sect1_info) + "\n"
        write_mapping_log("Get_Images_Content.txt", sect1_info)
        print bookname,title

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
        # print bookname+"_"+image,bookname, title, cat, image, page, del_blank_char(sect2_info)

        sect2_info = bookname+"_"+image+"\t"+bookname + "\t" + title + "\t" + cat + "\t" + image + "\t" + page + "\t" + del_blank_char(sect2_info) + "\n"
        write_mapping_log("Get_Images_Content.txt", sect2_info)
        print bookname,title

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
                    else:
                        if tag.name == 'para':
                            for string in tag.strings:
                                if str(string).isdigit():
                                    continue
                                sect3_info = sect3_info + string

        # print bookname+"_"+image,bookname, title, cat, image, page, del_blank_char(sect3_info)
        sect3_info = bookname+"_"+image+"\t"+bookname + "\t" + title + "\t" + cat + "\t" + image + "\t" + page + "\t" + del_blank_char(sect3_info) + "\n"
        write_mapping_log("Get_Images_Content.txt", sect3_info)
        print bookname,title

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
                    else:
                        if tag.name == 'para':
                            for string in tag.strings:
                                if str(string).isdigit():
                                    continue
                                sect4_info = sect4_info + string
        # print bookname+"_"+image,bookname,title, cat, image, page, del_blank_char(sect4_info)

        sect4_info = bookname+"_"+image+"\t"+bookname + "\t" + title + "\t" + cat + "\t" + image + "\t" + page + "\t" + del_blank_char(sect4_info) + "\n"
        write_mapping_log("Get_Images_Content.txt", sect4_info)
        print bookname,title

    def get_content(ptag):
        """
        获取标签下的正文信息
        : ptag 直接父级标签
        :return:
        """
        tag = ptag.name

        if tag == 'part':
            get_part_chapter_content()
        # 一级标签：preface 序
        elif tag == 'preface':
            get_chapter_content()
        # 一级标签：bibliography 参考文献
        elif tag == 'bibliography':
            get_chapter_content()
        # 一级标签：colophon 后记
        elif tag == 'colophon':
            get_chapter_content()
        # 一级标签：dedication 前言
        elif tag == 'dedication':
            get_chapter_content()
        # 一级标签：index 索引
        elif tag == 'index':
            get_chapter_content()
        # 一级标签：appendix 附录
        elif tag == 'appendix':
            get_chapter_content()
        # 一级标签&二级标签chapter
        elif tag == 'chapter':
            if ptag.parent.name == 'part':
                get_chapters_content(ptag)
            else:
                get_chapter_content()
        elif tag == 'sect1':
            xmlid = ptag.find('title').get('xml:id')
            get_sect1_content(xmlid)
        elif tag == 'sect2':
            xmlid = ptag.find('title').get('xml:id')
            get_sect2_content(xmlid)
        elif tag == 'sect3':
            xmlid = ptag.find('title').get('xml:id')
            get_sect3_content(xmlid)
        elif tag == 'sect4':
            xmlid = ptag.find('title').get('xml:id')
            get_sect4_content(xmlid)

    #1.先找表格
    tables = soup.find_all('table')


    # 处理标题
    if len(tables) > 0:
        # 处理标题
        title_list = list()
        for table in tables:
            if table.title.string is None:
                title = '暂无标题'
            else:
                title = table.title.string
            title_list.append(title)
        for i in range(len(title_list)):
            if title_list[i] == '续表':
                if title_list[i - 1] == '暂无标题':
                    title_list[i] = '续表'
                else:
                    title_list[i] = title_list[i - 1] + '续表'
        title_new_list = list()
        for title in title_list:
            if title.count('续表') > 1:
                title_new_list.append(title[:title.find('续表')] + '续表')
            else:
                title_new_list.append(title)

        # 提取信息
        for i in range(len(tables)):
            cat = tables[i].mediaobject.imageobject.get('role')
            if cat is None:
                cat = '暂无'
            # image = tables[i].mediaobject.imageobject.imagedata.get('fileref')[10:]
            image = tables[i].mediaobject.imageobject.imagedata.get('fileref')[7:]
            page = image[1:image.find("_")]
            title = title_new_list[i]
            print "父级标签为：", tables[i].parent.name
            get_content(tables[i].parent)



    # 2.再找图表
    pics = soup.find_all('mediaobject')
    if len(pics) > 0:
        for pic in pics:
            if pic.parent.name == 'table':
                continue
            cat = pic.imageobject.get('role')
            if cat is None:
                cat = '暂无'
            # image = pic.imageobject.imagedata.get('fileref')[10:]
            image = pic.imageobject.imagedata.get('fileref')[7:]
            page = image[1:image.find("_")]
            title = '暂无标题'
            if pic.parent.name == 'figure':
                title = pic.parent.title.string
                if title is None:
                    for string in pic.parent.title.strings:
                        title = string.strip()
                        break
                    if title is None:
                        title = '暂无标题'

            # 查找mediaobject的父级标签：
            print "父级标签为：", pic.parent.name
            if pic.parent.name == 'figure':
                get_content(pic.parent.parent)
            else:
                get_content(pic.parent)


def get_all_image_relate_content(srcdir):
    """
    :return:
    """
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir, filename)
        if os.path.isdir(file):
            get_all_image_relate_content(file)
        else:
            if filename.endswith("xml"):
                get_image_relate_content(file)


def main():
    # 配置数据
    # srcdir = u"E:\Goosuu\JinRong\Script\Deal-Middle\Chapter_XML\第一批数据"
    srcdir = u"E:\Goosuu\JinRong\Script\Deal-Middle\Chapter_XML\第二批数据"
    get_all_image_relate_content(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
