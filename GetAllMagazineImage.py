# coding=utf-8
"""
@Project: JinRong
@Time: 2019/1/4 9:56
@Name: GetAllMagazineImage
@Author: lieyan123091
"""

import os
import sys
import shutil
from PIL import Image

DEAL_MIDDILE_DIR = "I:\\Deal-Middle\\"
COVER_DIR = DEAL_MIDDILE_DIR + "Covers\\"
BookImage_DIR = DEAL_MIDDILE_DIR + "Book_Image\\"
FILE_IMAGE_EXTENSION = ".jpg"


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))


def get_all_image_files_from_dir(srcdir, folder='期刊'):
    """
    提取所有的图片，封面图片放到Covers文件夹，其余图片放到Images文件夹
    :param srcdir:
    :return:
    """
    coverfolder = COVER_DIR
    if not os.path.exists(coverfolder):
        os.makedirs(coverfolder)
    destfolder = BookImage_DIR + (folder).decode("utf-8").encode("gbk")
    if not os.path.exists(destfolder):
        os.makedirs(destfolder)
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir, filename)
        if os.path.isdir(file):
            # 排除epub文件夹下的images文件夹
            if file.endswith("epub"):
                continue
            get_all_image_files_from_dir(file)
        else:
            if filename.endswith(".jpg"):
                (filepath, name) = os.path.split(file)
                y_m_dir = os.path.dirname(filepath)[os.path.dirname(filepath).rfind("\\") + 1:]
                year_and_month = y_m_dir[-6:]
                if y_m_dir.endswith("2018-08-11中国金融201019-20"):
                    year_and_month = y_m_dir[-9:]
                cat_dir = os.path.dirname(os.path.dirname(os.path.dirname(filepath)))[
                          os.path.dirname(os.path.dirname(os.path.dirname(filepath))).rfind("\\") + 1:]
                if cat_dir.rfind("-") > -1:
                    catname = cat_dir[:cat_dir.rfind("-")]
                else:
                    catname = cat_dir
                bookname = catname + year_and_month
                if filename.endswith("cover.jpg"):
                    # 提取封面图片
                    destfile = COVER_DIR + bookname + FILE_IMAGE_EXTENSION
                    info = file + "\t" + destfile + "\t" + bookname + "\n"
                    write_mapping_log("Cover_Mapping.txt", info)
                else:
                    newfolder = BookImage_DIR + folder + "\\" + bookname
                    if not os.path.exists(newfolder):
                        os.makedirs(newfolder)
                    destfile = newfolder + "\\" + name
                    # 获取图片的详细信息
                    filesize = os.path.getsize(file)
                    img = Image.open(file)
                    info = bookname + "_" + name + "\t" + bookname + "\t" + name + "\t" + str(filesize) + "\t" + str(
                        img.size[0]) + "\t" + str(img.size[1]) + "\n"
                    write_mapping_log("ALL_MAGAZINE_IMAGE_File.txt", info)

                shutil.copy2(file, destfile)
                print file + " Copy Finished..."
                # print info


def main():
    srcdir = u"I:\\金融出版社书目\\期刊\\Source"
    get_all_image_files_from_dir(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()