# coding=utf-8
"""
@Project: JinRong
@Time: 2019/3/18 14:31
@Name: GetZhuanTiTongJiColorImage
@Author: lieyan123091
"""
import re, sys,os

def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))

regex_tab = re.compile("\\t")

i = 1

def get_images(srcfile):
    global i
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            guid = info[0].strip("\n")
            sql = 'UPDATE `report_img` set v_color = "彩色" where v_book_guid = \"%s\";'
            sql = sql % (guid)
            write_mapping_log("Zhuanti_report_color_images_info.sql",sql+"\n")
            print i,sql
            i = i + 1




def main():
    srcfile = u"color_guid.txt"
    get_images(srcfile)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()