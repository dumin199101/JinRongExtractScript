# coding=utf-8
"""
获取Image源文件
"""
import os
import sys


def get_all_image_files_from_dir(srcdir, type_set):
    """
    打印图片格式类型：只有P、T两种类型
    :param srcdir:
    :return:
    """
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir, filename)
        if os.path.isdir(file):
            get_all_image_files_from_dir(file, type_set)
        else:
            if filename.endswith(".jpg"):
                if not filename.endswith("cover.jpg"):
                    (filepath, name) = os.path.split(file)
                    name = name[:1]
                    type_set.add(name)
    return type_set


def main():
    srcdir = u"E:\\Goosuu\\JinRongSource\\第一批数据"
    type_set = set()
    types = get_all_image_files_from_dir(srcdir, type_set)
    for type in types:
        print type



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
