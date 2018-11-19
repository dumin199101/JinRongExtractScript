# coding=utf-8
"""
获取PDF源文件
"""
import os
import sys
import shutil


ROOTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))
RESULTDIR = ROOTDIR + "\\Result\\"
FILE_PDF_EXTENSION = ".pdf"


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))

# 配置数据
def get_all_pdf_files_from_dir(srcdir,folder='第三批数据'):
    """
    提取所有的PDF源文件，文件名重命名为当前文件夹名，并形成参照文件PDF_File.txt
    :param srcdir:
    :return:
    """
    destfolder = RESULTDIR + (folder).decode("utf-8").encode("gbk")
    if not os.path.exists(destfolder):
        os.makedirs(destfolder)
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir,filename)
        if os.path.isdir(file):
            get_all_pdf_files_from_dir(file)
        else:
            if filename.endswith(".pdf"):
                if filename.endswith("H.pdf"):
                    (filepath, name) = os.path.split(file)
                    dirname = os.path.dirname(filepath)
                    end_index = dirname.rfind('\\')
                    bookname = dirname[end_index + 1:]
                    destfile = RESULTDIR + folder + "\\" + bookname + FILE_PDF_EXTENSION
                    info = file + "\t" + destfile + "\t" + bookname + "\n"
                    write_mapping_log("PDF_FILE.txt", info)
                    shutil.copy2(file, destfile)
                    print file + " Copy Finished..."
                elif not filename.endswith("L.pdf"):
                    write_mapping_log("PDF.error.log.txt",file+"\n")









def main():
    # 配置数据
    # srcdir = u"E:\\Goosuu\\JinRongSource\\第一批数据"
    # srcdir = u"E:\\Goosuu\\JinRongSource\\第二批数据"
    srcdir = u"E:\\Goosuu\\JinRongSource\\第三批数据"
    get_all_pdf_files_from_dir(srcdir)



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()