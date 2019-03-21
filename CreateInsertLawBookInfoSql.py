# coding=utf-8
"""
@Project: JinRong
@Time: 2019/3/21 11:09
@Name: CreateInsertLawBookInfoSql
@Author: lieyan123091
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

def get_zhuanti_book_info(srcfile,prefix):
    global i
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            sql = 'INSERT INTO `'+prefix+'_title_info`(`v_guid`,`v_book_guid`,`v_title`,`n_startpage`,`n_endpage`,`n_pubdate`,`v_tag`,`v_category`,`v_industry`,`v_organization`,`v_unit`,`v_pubdate`,`v_timeliness`,`v_level`,`v_word`,`v_matetime`) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");'
            sql = sql % (info[0], info[1], info[3], info[4], info[5],info[16],info[6],info[7],info[8],info[9],info[10],info[11],info[12],info[13],info[14],info[15])
            print i,sql
            i = i + 1
            write_mapping_log(prefix + "_title_info.sql", sql + "\n")

def update_info(srcfile):
    global i
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            guid = info[0]
            # sql = 'UPDATE `law_title_info` AS a,`tb_title_info` AS b set a.v_filesize = b.v_filesize where a.v_guid = b.v_guid and a.v_guid = \"%s\";'
            # sql = 'UPDATE `law_title_info` AS a,`tb_title_info` AS b set a.n_browse_count = b.n_browse_count where a.v_guid = b.v_guid and a.v_guid = \"%s\";'
            sql = 'UPDATE `law_title_info` AS a,`tb_title_info` AS b set a.n_download_count = b.n_download_count where a.v_guid = b.v_guid and a.v_guid = \"%s\";'
            sql = sql % guid
            print i,sql
            i = i + 1
            # write_mapping_log("update_filesize.sql",sql+"\n")
            write_mapping_log("update_download_count.sql",sql+"\n")

def select_info(srcfile,prefix):
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            guid = info[0]
            sql = 'INSERT INTO `' + prefix + '_title_content` SELECT * FROM `tb_title_content` where v_guid = \"%s\";'
            sql = sql % (guid)
            print sql
            write_mapping_log(prefix + "_title_content.sql", sql + "\n")


def main():
    # srcfile = "law_title.txt"
    # prefix = 'law'
    # get_zhuanti_book_info(srcfile,prefix)


    srcfile = "law_title_old.txt"
    # update_info(srcfile)
    prefix = "law"
    select_info(srcfile,prefix)



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()