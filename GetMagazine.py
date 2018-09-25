# coding=utf-8
"""
@Project: JinRong
@Time: 2018/9/25 10:56
@Name: GetMagazine
@Author: lieyan123091
"""
import os
import sys
import shutil


ROOTDIR = "I:\\Deal-Middle"
RESULTDIR = ROOTDIR + "\\Magazine\\"
FILE_PDF_EXTENSION = ".pdf"


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))

# 配置数据
def get_all_magazine_files_from_dir(srcdir,folder='第一批数据'):
    """
    提取所有期刊数据的PDF源文件，文件名重命名为当前文件夹名，并形成参照文件MAGAZINE_FILE.txt
    :param srcdir:
    :return:
    """
    destfolder = RESULTDIR + (folder).decode("utf-8").encode("gbk")
    if not os.path.exists(destfolder):
        os.makedirs(destfolder)
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir,filename)
        if os.path.isdir(file):
            get_all_magazine_files_from_dir(file)
        else:
            if filename.endswith(".PDF") or (filename.endswith(".pdf") and (not filename.startswith("article")) and (not filename.startswith("articel")) and (not filename.startswith("artilce")) and (not filename.startswith("aricle"))):
                    (filepath, name) = os.path.split(file)
                    srcname = os.path.dirname(filepath)
                    dirname = os.path.dirname(os.path.dirname(os.path.dirname(filepath)))
                    end_index = dirname.rfind('\\')
                    srcname_1 = dirname[end_index + 1:]
                    if srcname_1.startswith("中国金融"):
                        _index = srcname_1.rfind("-")
                        srcname_1 = srcname_1[:_index]
                    bookname = srcname_1+srcname[-6:]
                    destfile = RESULTDIR + folder + "\\" + bookname + FILE_PDF_EXTENSION
                    info = file + "\t" + destfile + "\t" + bookname + "\n"
                    write_mapping_log("MAGAZINE_FILE.txt", info)
                    shutil.copy2(file, destfile)
                    print file + " Copy Finished..."

def main():
    # 配置数据
    srcdir = u"I:\\金融出版社书目\\期刊\\BaiduNetdiskDownload"
    get_all_magazine_files_from_dir(srcdir)





if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()