# coding=utf-8
"""
@Project: JinRong
@Time: 2018/12/24 15:17
@Name: GetMagazineXml
@Author: lieyan123091
"""
import os
import sys
import shutil


ROOTDIR = "I:\\Deal-Middle"
RESULTDIR = ROOTDIR + "\\MagazineXML\\"
FILE_PDF_EXTENSION = ".xml"


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))

# 配置数据
def get_all_magazine_xml_from_dir(srcdir,folder='第一批数据'):
    """
    提取所有期刊数据的PDF的xml源文件，文件名重命名为当前文件夹名，并形成参照文件MAGAZINE_XML_FILE.txt
    :param srcdir:
    :return:
    """
    destfolder = RESULTDIR + (folder).decode("utf-8").encode("gbk")
    if not os.path.exists(destfolder):
        os.makedirs(destfolder)
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir,filename)
        if os.path.isdir(file):
            get_all_magazine_xml_from_dir(file)
        else:
            if filename.endswith("index.xml"):
                    (filepath, name) = os.path.split(file)
                    dirname = os.path.dirname(os.path.dirname(filepath))
                    end_index = dirname.rfind('\\')
                    srcname_1 = dirname[end_index + 1:]
                    if srcname_1.startswith("中国金融"):
                        _index = srcname_1.rfind("-")
                        srcname_1 = srcname_1[:_index]
                    bookname = srcname_1+filepath[-6:]
                    destfile = RESULTDIR + folder + "\\" + bookname + FILE_PDF_EXTENSION
                    info = file + "\t" + destfile + "\t" + bookname + "\n"
                    write_mapping_log("MAGAZINE_XML_FILE.txt", info)
                    shutil.copy2(file, destfile)
                    print file + " Copy Finished..."

def main():
    # 配置数据
    srcdir = u"I:\\金融出版社书目\\期刊\\Source"
    get_all_magazine_xml_from_dir(srcdir)





if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
