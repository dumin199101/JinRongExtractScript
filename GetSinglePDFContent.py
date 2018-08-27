# coding=utf-8
"""
@Project: JinRong
@Time: 2018/8/27 9:57
@Name: GetSinglePDFContent
@Author: lieyan123091
"""

import sys, re


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))


def get_level1_content(filename):
    """
    第一步：提取层级为1的文本
    :param filename:
    :return:
    """
    re_tab = re.compile("\\t")
    with open(filename) as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = re_tab.split(line)
            if info[2].find('-') == -1:
                write_mapping_log("Content_Level1_File.txt", info[0] + "\t" + info[1] + "\t" + info[2] + "\t" + info[6])
                print info[0], info[1]


def get_single_pdf_content(filename):
    """
    第二步：组合层级为1的文本，获取单本PDF的正文文本
    :param filename:
    :return:
    """
    re_tab = re.compile("\\t")
    with open(filename) as f1:
        line_1st = f1.readline()
        info = ''
        while True:
            if len(line_1st) < 1:
                break
            line_2nd = f1.readline()
            (fields1st) = re_tab.split(line_1st)
            line_1st_level = int(fields1st[2])
            if len(line_2nd) > 1:
                (fields2nd) = re_tab.split(line_2nd)
                line_2nd_level = int(fields2nd[2])
                if line_2nd_level < line_1st_level:
                    # 到达临界点
                    print fields1st[0], fields1st[1]
                    info = info + fields1st[3].strip()
                    write_mapping_log("Content_PDF_File.txt", fields1st[0] + "\t" + info + "\n")
                    info = ''
                else:
                    info = info + fields1st[3].strip()
                line_1st = line_2nd
            else:
                # 到达最后一行
                info = info + fields1st[3].strip()
                print fields1st[0], fields1st[1]
                write_mapping_log("Content_PDF_File.txt", fields1st[0] + "\t" + info + "\n")
                break


def main():
    # Step1:配置数据：
    txtfile = u"Content_File.txt"
    get_level1_content(txtfile)

    # Step2:配置数据：
    txtfile = u"Content_Level1_File.txt"
    get_single_pdf_content(txtfile)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
