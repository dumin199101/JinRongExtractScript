# coding=utf-8
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


def get_pic_from_xml(soup, file):
    """
    从xml文件中提取图片信息
    :param soup:
    :param file:
    :return:
    """
    (filepath, name) = os.path.split(file)
    dirname = filepath
    end_index = dirname.rfind('\\')
    bookname = dirname[end_index + 1:]

    # 1.先找表格
    tables = soup.find_all('table')

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
            print bookname, image
            level = get_level_tree(tables[i], soup)
            # print bookname, image, title, cat, page, level
            write_mapping_log("All_Image_Info.txt",
                              bookname + "_" + image + "\t" + bookname + "\t" + image + "\t" + title + "\t" + cat + "\t" + page + "\t" + level + "\n")

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

            print bookname, image
            level = get_level_tree(pic, soup)
            # print bookname, image, title, cat, page, level
            write_mapping_log("All_Image_Info.txt",
                              bookname + "_" + image + "\t" + bookname + "\t" + image + "\t" + title + "\t" + cat + "\t" + page + "\t" + level + "\n")


def get_level_tree(obj, soup):
    """
       获取层级树
       :return:
    """

    def get_chapt_info(chapt):
        title = chapt.select('info > title')[0].string
        if title is None:
            for string in chapt.title.strings:
                title = string
                break
        return title


    def get_title(tag):
        title = tag.select('info > title')[0].string
        if title is None:
            for string in tag.select('info > title')[0].strings:
                title = string
                break
        return title.strip()

    def get_chapter_title():
        """
        查询章节title
        :return:
        """
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
            title = soup.select('part > info > title')[0].string
            # 这种情况是处理title标签中有多个标签的情况
            if title is None:
                for string in soup.title.strings:
                    title = string
                    break
        elif len(chapter) == 1:
            # 从info标签中获取基本信息
            title = soup.select('chapter > info > title')[0].string
            if title is None:
                for string in soup.title.strings:
                    title = string
                    break
        elif len(chapter) > 1:
            chapt = obj.parent.parent
            if chapt.name == 'chapter':
                title = get_chapt_info(chapt)
        elif len(bibliography) > 0:
            # 从info标签中获取基本信息
            title = soup.select('bibliography > blockquote > info > title')[0].string
            if title is None:
                for string in soup.title.strings:
                    title = string
                    break
        elif len(preface) > 0:
            # 从info标签中获取基本信息
            title = soup.select('preface > info > title')[0].string
            if title is None:
                for string in soup.title.strings:
                    title = string
                    break
        elif len(colophon) > 0:
            # 从info标签中获取基本信息
            title = soup.select('colophon > info > title')[0].string
            if title is None:
                for string in soup.title.strings:
                    title = string
                    break
        elif len(dedication) > 0:
            # 从info标签中获取基本信息
            title = soup.select('dedication > info > title')[0].string
            # 这种情况是处理title标签中有多个标签的情况
            if title is None:
                for string in soup.title.strings:
                    title = string
                    break
        elif len(index) > 0:
            title = soup.select('index > info > title')[0].string
            # 这种情况是处理title标签中有多个标签的情况
            if title is None:
                for string in soup.title.strings:
                    title = string
                    break
        elif len(appendix) > 0:
            title = soup.select('appendix > info > title')[0].string
            # 这种情况是处理title标签中有多个标签的情况
            if title is None:
                for string in soup.title.strings:
                    title = string
                    break

        return title.strip()

    name = obj.parent.name
    chapter = get_chapter_title()

    # 父类是二级标题
    if name == 'sect1':
        level_1 = get_title(obj.parent)
        level = chapter + "_" + level_1
    # 父类是三级标题
    elif name == 'sect2':
        level_2 = get_title(obj.parent)
        sect1_obj = obj.parent.parent
        level_1 = get_title(sect1_obj)
        level = chapter + "_" + level_1 + '_' + level_2
    # 父类是四级标题
    elif name == 'sect3':
        level_3 = get_title(obj.parent)
        sect2_obj = obj.parent.parent
        sect1_obj = sect2_obj.parent
        level_2 = get_title(sect2_obj)
        level_1 = get_title(sect1_obj)
        level = chapter + "_" + level_1 + '_' + level_2 + '_' + level_3
    # 父类是五级标题
    elif name == 'sect4':
        level_4 = get_title(obj.parent)
        sect3_obj = obj.parent.parent
        sect2_obj = sect3_obj.parent
        sect1_obj = sect2_obj.parent
        level_3 = get_title(sect3_obj)
        level_2 = get_title(sect2_obj)
        level_1 = get_title(sect1_obj)
        level = chapter + "_" + level_1 + '_' + level_2 + '_' + level_3 + '_' + level_4
    elif name == 'figure':
        figure_tag = obj.parent
        pname = figure_tag.parent.name
        if pname == 'sect4':
            level_4 = get_title(obj.parent.parent)
            sect3_obj = obj.parent.parent.parent
            level_3 = get_title(sect3_obj)
            sect2_obj = sect3_obj.parent.parent
            sect1_obj = sect2_obj.parent.parent
            level_2 = get_title(sect2_obj)
            level_1 = get_title(sect1_obj)
            level = chapter + "_" + level_1 + '_' + level_2 + '_' + level_3 + '_' + level_4
            return level
        if pname == 'sect3':
            level_3 = get_title(obj.parent.parent)
            sect2_obj = obj.parent.parent.parent
            sect1_obj = sect2_obj.parent.parent
            level_2 = get_title(sect2_obj)
            level_1 = get_title(sect1_obj)
            level = chapter + "_" + level_1 + '_' + level_2 + '_' + level_3
        elif pname == 'sect2':
            level_2 = get_title(obj.parent.parent)
            sect1_obj = obj.parent.parent.parent
            level_1 = get_title(sect1_obj)
            level = chapter + "_" + level_1 + '_' + level_2
        elif pname == 'sect1':
            level_1 = get_title(obj.parent.parent)
            level = chapter + "_" + level_1
        else:
            level = chapter
    else:
        level = chapter

    return level


def get_image_info(file):
    """
    获取图片基本信息
    :param file:
    :return:
    """
    # 配置数据
    soup = BeautifulSoup(open(file.encode("gbk")), features='xml')
    get_pic_from_xml(soup, file)


def get_all_image_info(srcdir):
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir, filename)
        if os.path.isdir(file):
            get_all_image_info(file)
        else:
            if filename.endswith("xml"):
                get_image_info(file)


def main():
    # 配置数据
    # srcdir = u"E:\Goosuu\JinRong\Script\Deal-Middle\Chapter_XML\第一批数据"
    srcdir = u"E:\Goosuu\JinRong\Script\Deal-Middle\Chapter_XML\第二批数据"
    get_all_image_info(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
