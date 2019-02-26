# coding=utf-8
"""
@Project: JinRong
@Time: 2019/2/14 10:42
@Name: GetMagazineColumnMapping
@Author: lieyan123091
"""
# coding=utf-8
import os
import sys
from bs4 import BeautifulSoup
import re


def del_blank_char(str):
    """
    去除字符串中的空白跟换行符
    :param str:
    :return:
    """
    rep = re.compile(r'(\n|\t|\s+)')
    (fstr, count) = rep.subn('', str)
    return fstr


ROOTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))

i = 0

def get_magazine_catalog(file):
    (filepath, name) = os.path.split(file)
    (bookname, extension) = os.path.splitext(name)
    if bookname.endswith("中国金融201019-20"):
        cat_name = bookname[:-9]
        year = bookname[-9:-5]
        order = bookname[-5:]
    else:
        cat_name = bookname[:-6]
        year = bookname[-6:-2]
        order = bookname[-2:]
    soup = BeautifulSoup(open(file.encode("gbk")), features='xml')
    print name


    # # 第②部分信息：magazineforum,magazinecolumns,magazinecolumn
    magazineforums = soup.select("magazineforum")
    # 一级标签获取
    for chapter in magazineforums:
        # global i
        name_tag = chapter.find('name')
        if name_tag.string is None or name_tag.string.strip() == '':
            magazinecolumn_tags = chapter.magazinecolumns.find_all('magazinecolumn')
            for magazinecolumn_tag in magazinecolumn_tags:
                # 去除空白字符
                if magazinecolumn_tag.find('name').string is not None and len(magazinecolumn_tag.find('name').string.strip())>0:
                    # print "*" * 10, del_blank_char(magazinecolumn_tag.find('name').string)
                    # i = i + 1

                    # ①获取栏目
                    # write_mapping_log("Magazine_Catalog_Mapping.txt", cat_name + "\t" + cat_name + "_" + del_blank_char(
                    #     magazinecolumn_tag.find('name').string) + "\t" + bookname + "\t" + str(
                    #     1) + "\t" + "顶级栏目" + "\t" + del_blank_char(magazinecolumn_tag.find('name').string) + "\n")

                    # ②获取目录结构
                    # write_mapping_log("MagazineCatalog.txt",cat_name+"\t"+ "*-*" + "\t" + del_blank_char(magazinecolumn_tag.find('name').string)+"\t"+str(1)+"\t"+bookname+"\t"+year+"\t"+order+"\t"+"*-*"+"\n")


                    # 获取二级标签
                    docs_tag = magazinecolumn_tag.docs.find_all('doc')
                    for doc_tag in docs_tag:
                        id = doc_tag.id.string
                        title = doc_tag.front.title.string
                        if title is None:
                            title = ''
                            for string in doc_tag.front.title.strings:
                                title = title + string
                        pageRange = doc_tag.content.find(role="pdfpage").string
                        # print "*" * 20, bookname,id, title, pageRange

                        # ② 获取目录结构
                        # write_mapping_log("MagazineCatalog.txt", cat_name + "\t" + id + "\t" + title + "\t" + str(
                        #     2) + "\t" + bookname + "\t" + year + "\t" + order + "\t" + pageRange + "\n")

                        # ③获取栏目-标题映射关系
                        write_mapping_log("MagazineColumnMappingRefer.txt", cat_name + "_" + del_blank_char(
                            magazinecolumn_tag.find('name').string) + "\t" + bookname + "_" + id + "_" + title  + "\n")
                else:
                    # 一级标签为None
                    # 获取二级标签
                    docs_tag = magazinecolumn_tag.docs.find_all('doc')
                    for doc_tag in docs_tag:
                        id = doc_tag.id.string
                        title = doc_tag.front.title.string
                        if title is None:
                            title = ''
                            for string in doc_tag.front.title.strings:
                                title = title + string
                        pageRange = doc_tag.content.find(role="pdfpage").string
                        # print "*" * 20, bookname,id, title, pageRange

                        # ② 获取目录结构
                        # write_mapping_log("MagazineCatalog.txt", cat_name + "\t" + id + "\t" + title + "\t" + str(
                        #     2) + "\t" + bookname + "\t" + year + "\t" + order + "\t" + pageRange + "\n")

                        # ③获取栏目-标题映射关系
                        write_mapping_log("MagazineColumnMappingRefer.txt", cat_name + "_" + '暂无栏目'+ "\t" + bookname + "_" + id + "_" + title + "\n")



        else:
            # print "*" * 10, name_tag.string
            # i = i + 1
            # ①获取栏目
            # write_mapping_log("Magazine_Catalog_Mapping.txt",
            #                   cat_name + "\t" + cat_name + "_" + name_tag.string + "\t" +
            #                   bookname + "\t" + str(1) + "\t" + "顶级栏目" + "\t" + name_tag.string + "\n")

            # ②获取目录结构
            # write_mapping_log("MagazineCatalog.txt", cat_name + "\t" + "*-*" + "\t" + name_tag.string + "\t" + str(
            #     1) + "\t" + bookname + "\t" + year + "\t" + order + "\t" + "*-*" + "\n")

            # 获取二级标签
            magazinecolumn_tags = chapter.magazinecolumns.find_all('magazinecolumn')
            for magazinecolumn_tag in magazinecolumn_tags:
                if magazinecolumn_tag.find('name').string is not None and len(magazinecolumn_tag.find('name').string.strip())>0:
                    # print "*" * 20, magazinecolumn_tag.find('name').string
                    # i = i + 1
                    # ①获取栏目
                    # write_mapping_log("Magazine_Catalog_Mapping.txt",
                    #                   cat_name + "\t" + cat_name + "_" + del_blank_char(
                    #                       magazinecolumn_tag.find('name').string) + "\t" +
                    #                   bookname + "\t" + str(2) + "\t" + name_tag.string + "\t" + del_blank_char(
                    #                       magazinecolumn_tag.find('name').string) + "\n")

                    # ②获取目录结构
                    # write_mapping_log("MagazineCatalog.txt", cat_name + "\t" + "*-*" + "\t" + del_blank_char(
                    #                       magazinecolumn_tag.find('name').string) + "\t" + str(
                    #     2) + "\t" + bookname + "\t" + year + "\t" + order + "\t" + "*-*" + "\n")


                    # 获取三级标签
                    docs_tag = magazinecolumn_tag.docs.find_all('doc')
                    for doc_tag in docs_tag:
                        id = doc_tag.id.string
                        title = doc_tag.front.title.string
                        if title is None:
                            title = ''
                            for string in doc_tag.front.title.strings:
                                title = title + string
                        pageRange = doc_tag.content.find(role="pdfpage").string

                        #②获取目录结构
                        # write_mapping_log("MagazineCatalog.txt", cat_name + "\t" + id + "\t" + title + "\t" + str(
                        #     3) + "\t" + bookname + "\t" + year + "\t" + order + "\t" + pageRange + "\n")

                        # ③获取栏目-标题映射关系
                        write_mapping_log("MagazineColumnMappingRefer.txt", cat_name + "_" + del_blank_char(
                            magazinecolumn_tag.find(
                                'name').string) + "\t"  + bookname + "_" + id + "_" + title + "\n")

                else:
                    # 二级标签为None的情况
                    # 获取三级标签
                    docs_tag = magazinecolumn_tag.docs.find_all('doc')
                    for doc_tag in docs_tag:
                        id = doc_tag.id.string
                        title = doc_tag.front.title.string
                        if title is None:
                            title = ''
                            for string in doc_tag.front.title.strings:
                                title = title + string
                        pageRange = doc_tag.content.find(role="pdfpage").string

                        # ②获取目录结构
                        # write_mapping_log("MagazineCatalog.txt", cat_name + "\t" + id + "\t" + title + "\t" + str(
                        #     3) + "\t" + bookname + "\t" + year + "\t" + order + "\t" + pageRange + "\n")

                        # ③获取栏目-标题映射关系
                        write_mapping_log("MagazineColumnMappingRefer.txt", cat_name + "_" + "暂无栏目" + "\t"  + bookname + "_" + id + "_" + title + "\n")





def get_magazine_catalogs(srcdir):
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir, filename)
        if filename.endswith("xml"):
            get_magazine_catalog(file)


def main():
    srcdir = u"J:\\Deal-Middle\\期刊数据\\EXTRACTCDATAXML"
    get_magazine_catalogs(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()