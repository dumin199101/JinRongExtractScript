# coding=utf-8
"""
@Project: JinRong
@Time: 2018/9/18 14:50
@Name: GetBlankPDFDirSet
@Author: lieyan123091
"""

import sys
import os


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))


def get_blank_pdf_dir_set(srcdir):
    """
    获取pdf缺失的目录
    :param srcdir:
    :return:
    """
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir, filename)
        if os.path.isdir(file):
            # 统计文件夹个数:符合标准的个数为4：dpdf，epub，images，xml
            length = len([name for name in os.listdir(file) if os.path.isdir(os.path.join(file, name))])
            if (length != 4) and (not file.endswith("dpdf") and not file.endswith("epub") and not file.endswith(
                    "images") and not file.endswith("xml")):
                print file
            if length == 4:
                print file, length
            # 统计文件个数：存在dpdf文件夹，并且pdf文件数为2
            length = len([name for name in os.listdir(file) if os.path.isfile(os.path.join(file, name))])
            if length == 2 and file.endswith("dpdf"):
                print file,length
            print file, length
            get_blank_pdf_dir_set(file)
        else:
            # 删除Thumbs.db文件
            if filename.endswith(".db"):
                os.remove(file)
                print file + " delete Successfully..."
            # 查找有误数据
            if not file.endswith(".pdf") and not file.endswith(".jpg") and not file.endswith(".png") and not file.endswith(".xml") and not file.endswith(".epub"):
                print file


def main():
    # 配置数据
    srcdir = u"E:\\Goosuu\\JinRongSource\\第二批数据"
    get_blank_pdf_dir_set(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
