# coding=utf-8
"""
@Project: JinRong
@Time: 2019/3/18 12:24
@Name: GetZhuanTiTongJiImagesInfo
@Author: lieyan123091
"""
import re, sys,os

SOURCE_DIR = "I:\\Finish-ZT\\2金融统计报告\\Images"


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
    global i,j
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            guid = info[0]
            bookid = info[1]
            name = info[2].strip("\n")
            srcfolder = SOURCE_DIR.encode("gbk") + "\\" + bookid
            if os.path.exists(srcfolder):
                for file in os.listdir(srcfolder):
                    if file==name:
                        sql = 'INSERT INTO `report_img` SELECT * FROM `tb_image_info` where v_guid = \"%s\";'
                        sql = sql % (guid)
                        print i,sql
                        sql2 = 'INSERT INTO `report_img_content` SELECT * FROM `tb_image_content` where v_guid = \"%s\";'
                        sql2 = sql2 % (guid)
                        write_mapping_log("Zhuanti_report_images_info.sql",sql+"\n")
                        write_mapping_log("Zhuanti_report_images_content.sql",sql2+"\n")
                        # print i, bookid,name
                        i = i + 1


def main():
    srcfile = u"tb_image_info.txt"
    get_images(srcfile)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
