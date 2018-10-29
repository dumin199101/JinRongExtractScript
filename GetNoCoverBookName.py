# coding=utf-8
"""
@Project: JinRong
@Time: 2018/10/29 11:58
@Name: GetNoCoverBookName
@Author: lieyan123091
"""

# coding=utf-8
"""
获取缺少封面的文件夹
"""
import os
import sys

def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))


def get_no_cover_name_from_dir(srcdir):
    """
    提取所有的图片，封面图片放到Covers文件夹，其余图片放到Images文件夹
    :param srcdir:
    :return:
    """
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir, filename)
        if os.path.isdir(file):
            get_no_cover_name_from_dir(file)
            if file.endswith('images'):
                for root, dirs, files in os.walk(file):
                    if 'cover.jpg' not in files:
                        print root




def main():
    srcdir = u"E:\\Goosuu\\JinRongSource\\第二批数据"
    get_no_cover_name_from_dir(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
