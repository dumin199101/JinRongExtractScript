# coding=utf-8
"""
@Project: JinRong
@Time: 2019/1/4 14:19
@Name: GetMagazineImageInfo
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


def get_pic_from_xml(soup, file):
    """
    从xml文件中提取图片信息
    :param soup:
    :param file:
    :return:
    """
    (filepath, name) = os.path.split(file)
    bookname = name[:name.rfind(".xml")]

    # 找图表
    pics = soup.find_all('mediaobject')
    if len(pics) > 0:
        for pic in pics:
            image = pic.imageobject.imagedata.get('fileref')[7:]
            page = image[1:image.find("_")]
            title = '暂无标题'
            cat = '暂无'
            if pic.parent.name == 'figure':
                cat = pic.parent.get('role')
                if cat is None:
                    cat = '暂无'
                title = pic.parent.title.string
                if title is None:
                    for string in pic.parent.title.strings:
                        title = string.strip()
                        break
                    if title is None:
                        title = '暂无标题'

            print bookname, image, title, cat, page
            level = bookname + "_" + get_level_tree(pic)
            # print bookname, image, title, cat, page, level
            write_mapping_log("All_Image_Info.txt",
                              bookname + "_" + image + "\t" + bookname + "\t" + image + "\t" + title + "\t" + cat + "\t" + page + "\t" + level + "\n")


def get_level_tree(obj):
    """
       获取层级树
       :return:
    """
    for parent in obj.parents:
        if parent.name != 'doc':
            continue
        title = parent.select('front > title')[0].string
        if title is None:
            for string in parent.select('front > title')[0].strings:
                title = string
                break
        return title.strip()


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
    srcdir = u"I:\\Deal-Middle\\EXTRACTCDATAXML"
    get_all_image_info(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()