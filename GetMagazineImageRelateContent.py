# coding=utf-8
"""
@Project: JinRong
@Time: 2019/1/4 17:22
@Name: GetMagazineImageRelateContent
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
    rep = re.compile(r'(\n|\t|\r|\s+)')
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
    bookname = name[:name.rfind(".xml")]

    soup = BeautifulSoup(open(file.encode("gbk")), features='xml')

    # 声明一个集合统计标签种类：创建空集合必须使用set函数，非空集合可以使用{}
    tag_set = set()
    for tag in soup.find_all(True):
        tag_set.add(tag.name)


    def get_content(tag):
        for parent in tag.parents:
            if parent.name != 'doc':
                continue
            tag_allow_set = {'title', 'para'}
            info = ''
            for tag in parent.find_all(True):
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
                                if str(string).isdigit():
                                    continue
                                info = info + string
            # print bookname+"_"+image,bookname, title, cat, image, page, del_blank_char(info)
            content = del_blank_char(info)
            info = bookname+"_"+image+"\t"+bookname + "\t" + title + "\t" + cat + "\t" + image + "\t" + page + "\t" + content + "\n"
            write_mapping_log("Get_Magazine_Images_Content.txt", info)
            print bookname,title
            # print info

    #找图表
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
            get_content(pic)


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
    srcdir = u"I:\\Deal-Middle\\EXTRACTCDATAXML"
    get_all_image_relate_content(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()