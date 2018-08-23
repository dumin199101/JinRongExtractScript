# coding=utf-8
"""
解析目录XML信息
"""
import os
import sys
import xml.dom.minidom as xmldom


ROOTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))


def get_mulu_info(file):
    """
    根据提取的目录XML信息，提取目录信息（目录名称，开始页码，结束页码，文件名称，目录层级），并形成参照文件MULU_File.txt
    :return:
    """
    (srcdir,filename) = os.path.split(file)
    xmlfilepath = os.path.abspath(file.decode("utf-8").encode("gbk"))
    domobj = xmldom.parse(xmlfilepath)
    elementobj = domobj.documentElement
    """
    TitleElementObj1 = elementobj.getElementsByTagName("title")
    for i in range(len(TitleElementObj1)):
      if TitleElementObj1[i].firstChild.data.find('目录') < 0: # 排除目录
            print i,TitleElementObj1[i].firstChild.data  # 显示标签对之间的数据
    """
    DivElementObj1 = elementobj.getElementsByTagName("tocdiv")
    global info
    for i in range(len(DivElementObj1)):
        # 寻找子节点
        childNodes = DivElementObj1[i].childNodes
        for node in childNodes:
            if node.nodeName == '#text':  # 去除换行符
                continue
            else:
                if node.nodeName == 'title':
                    title = node.firstChild.data
                    info = title
                elif node.nodeName == 'tocentry':
                    pagenum = node.getAttribute('pagenum')
                    href = node.getAttribute('xlink:href')
                    # 对href进行拆分：得到文件位置跟目录层级
                    (fileaddr, chapter) = href.split("#")
                    # 统计目录层级
                    count = chapter.count("-")
                    chaptername = chapter[7:]
                    info = info + "\t" + filename[:-4] + "\t" + href + "\t" + fileaddr + "\t" + chapter + "\t" + chaptername + "\t" + str(
                        count + 1) + "\t" + pagenum + "\n"
        write_mapping_log("parseMuluXML.txt", info)
    print filename + " Get Info Success...."



def get_all_mulu_info_from_xml(srcdir):
    """
    从mulu_xml中获取信息
    :param srcdir:
    :return:
    """
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir,filename)
        get_mulu_info(file)






def main():
    srcdir = u'E:\Goosuu\JinRong\Script\Deal-Middle\MULU_XML\第一批数据'
    get_all_mulu_info_from_xml(srcdir)



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()