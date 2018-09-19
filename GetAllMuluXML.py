# coding=utf-8
"""
获取PDF源文件
"""
import os
import sys
import shutil


ROOTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))
MIDDLEDIR = ROOTDIR + "\\Deal-Middle\\"
MULU_XML_DIR = MIDDLEDIR + "MULU_XML\\"
FILE_XML_EXTENSION = ".xml"


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))

# 配置数据
def get_all_mulu_files_from_dir(srcdir,folder='第二批数据'):
    """
    提取所有的XML目录信息，文件名重命名为当前文件夹名，并形成参照文件XML_MULU_File.txt
    :param srcdir:
    :return:
    """
    destfolder = MULU_XML_DIR + (folder).decode("utf-8").encode("gbk")
    if not os.path.exists(destfolder):
        os.makedirs(destfolder)
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir,filename)
        if os.path.isdir(file):
            get_all_mulu_files_from_dir(file)
        else:
            if filename.endswith("1_toc.xml") or filename.endswith("1_toc(1).xml"):
                (filepath, name) = os.path.split(file)
                dirname  = os.path.dirname(filepath)
                end_index = dirname.rfind('\\')
                bookname = dirname[end_index+1:]
                destfile = MULU_XML_DIR + folder + "\\" + bookname + FILE_XML_EXTENSION
                info = file + "\t" + destfile + "\t" + bookname + "\n"
                write_mapping_log("XML_MULU_File.txt",info)
                shutil.copy2(file,destfile)
                print file + " Copy Finished..."
            elif filename.endswith(".xml") and not filename.startswith("2_chapter") and not filename.startswith("Main.xml"):
                write_mapping_log("PDF_Mulu_error.txt",file+"\n")





def main():
    # 配置数据
    # srcdir = u"E:\\Goosuu\\JinRongSource\\第一批数据"
    srcdir = u"E:\\Goosuu\\JinRongSource\\第二批数据"
    get_all_mulu_files_from_dir(srcdir)



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()