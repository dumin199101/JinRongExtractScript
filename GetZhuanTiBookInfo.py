# coding=utf-8
"""
@Project: JinRong
@Time: 2019/3/11 19:06
@Name: GetZhuanTiBookInfo
@Author: lieyan123091
获取专题基本信息
"""
import re, sys

def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))

regex_tab = re.compile("\\t")

i = 1
j = 1

# 第一步：筛选出专题v_book_name
def get_zhuanti_book_info(srcfile,zhuanti_str):
    global i,j
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            bookname = info[0]
            catname = info[1]
            if catname==zhuanti_str:
                print j,i,bookname
                write_mapping_log(u"zhuanti_"+zhuanti_str+".txt",str(i)+"\t"+bookname+"\n")
                j = j + 1
            i = i + 1


def create_get_zhuanti_book_info_sql(srcfile,prefix):
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            bookname = info[1].strip("\n")
            sql =  'INSERT INTO `'+prefix+'_book_info` SELECT * FROM `tb_book_info` where v_book_name = \"%s\";'
            sql = sql % (bookname)
            write_mapping_log(prefix+"_book_info.sql",sql+"\n")

def create_get_zhuanti_book_content_sql(srcfile,prefix):
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            guid = info[0]
            sql = 'INSERT INTO `'+prefix+'_book_content` SELECT * FROM `tb_book_content` where v_book_guid = \"%s\";'
            sql = sql % (guid)
            print sql
            write_mapping_log(prefix+"_book_content.sql", sql + "\n")


def create_get_zhuanti_title_info_sql(srcfile,prefix):
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            guid = info[0]
            sql = 'INSERT INTO `'+prefix+'_title_info` SELECT * FROM `tb_title_info` where v_book_guid = \"%s\";'
            sql = sql % (guid)
            print sql
            write_mapping_log(prefix+"_title_info.sql", sql + "\n")


def create_get_zhuanti_title_content_sql(srcfile,prefix):
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            guid = info[0]
            sql = 'INSERT INTO `'+prefix+'_title_content` SELECT * FROM `tb_title_content` where v_guid = \"%s\";'
            sql = sql % (guid)
            print sql
            write_mapping_log(prefix+"_title_content.sql", sql + "\n")


def create_get_zhuanti_title_content_sql(srcfile,prefix):
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            guid = info[0]
            sql = 'INSERT INTO `'+prefix+'_title_content` SELECT * FROM `tb_title_content` where v_guid = \"%s\";'
            sql = sql % (guid)
            print sql
            write_mapping_log(prefix+"_title_content.sql", sql + "\n")


def create_get_zhuanti_mulu_level_sql(srcfile,prefix):
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            guid = info[0]
            sql = 'INSERT INTO `'+prefix+'_mulu_level` SELECT * FROM `tb_mulu_level` where v_guid = \"%s\";'
            sql = sql % (guid)
            print sql
            write_mapping_log(prefix+"_mulu_level.sql", sql + "\n")







def main():
    # 第一步
    srcfile = u"category.txt"
    # zhuanti_str = '金融基本文献'
    # zhuanti_str = '金融统计分析'
    # zhuanti_str = '金融教育培训'
    # get_zhuanti_book_info(srcfile,zhuanti_str)

    # 第二步
    # srcfile = u"zhuanti_金融基本文献.txt"
    # prefix = 'literature'
    # srcfile = u"zhuanti_金融统计分析.txt"
    # prefix = 'report'
    # srcfile = u"zhuanti_金融教育培训.txt"
    # prefix = 'edu'
    # create_get_zhuanti_book_info_sql(srcfile,prefix)


    # 第三步
    # srcfile = u"literature_book_info_guid.txt"
    # prefix = 'literature'
    # srcfile = u"report_book_info_guid.txt"
    # prefix = 'report'
    # srcfile = u"edu_book_info_guid.txt"
    # prefix = 'edu'
    # create_get_zhuanti_book_content_sql(srcfile,prefix)

    # 第四步
    # srcfile = u"literature_book_info_guid.txt"
    # prefix = 'literature'
    # srcfile = u"report_book_info_guid.txt"
    # prefix = 'report'
    # srcfile = u"edu_book_info_guid.txt"
    # prefix = 'edu'
    # create_get_zhuanti_title_info_sql(srcfile,prefix)

    # 第五步
    # srcfile = u"literature_title_info_guid.txt"
    # prefix = 'literature'
    # srcfile = u"report_title_info_guid.txt"
    # prefix = 'report'
    # srcfile = u"edu_title_info_guid.txt"
    # prefix = 'edu'
    # create_get_zhuanti_title_content_sql(srcfile,prefix)

    # 第六步
    # srcfile = u"literature_title_info_guid.txt"
    # prefix = 'literature'
    # srcfile = u"report_title_info_guid.txt"
    # prefix = 'report'
    # srcfile = u"edu_title_info_guid.txt"
    # prefix = 'edu'
    # create_get_zhuanti_mulu_level_sql(srcfile,prefix)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()