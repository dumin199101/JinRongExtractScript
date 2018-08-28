# coding=utf-8
"""
获取Image源文件
"""
import os
import sys
import shutil
from PIL import Image

ROOTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))
RESULTDIR = ROOTDIR + "\\Result\\"
DEAL_MIDDILE_DIR = ROOTDIR + "\\Deal-Middle\\"
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


def get_all_image_files_from_dir(srcdir, folder='第一批数据'):
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
            get_all_image_files_from_dir(file)
        else:
            if filename.endswith(".jpg"):
                (filepath, name) = os.path.split(file)
                dirname = os.path.dirname(filepath)
                end_index = dirname.rfind('\\')
                bookname = dirname[end_index + 1:]
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
                    write_mapping_log("ALL_IMAGE_File.txt", info)

                shutil.copy2(file, destfile)
                print file + " Copy Finished..."
                # print info


def main():
    srcdir = u"E:\\Goosuu\\JinRongSource\\第一批数据"
    get_all_image_files_from_dir(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
