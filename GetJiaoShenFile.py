# coding=utf-8
import os
import sys
import re

ROOTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))


def read_mapping_log(logname):
    """
    读取log日志
    :param logname:
    :return:
    """
    with open(logname, "r") as f1:
        regex_tab = re.compile("\\t")
        while True:
            line = f1.readline().decode("utf-8")
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            string = info[0] + "\t" + info[1] + "\t" + info[5] + "\t" + info[6] + "\t" + info[7].strip('\n') + "\t" + info[1] + "_" + info[5] + "_" + info[0]  + "\t" + "\n"
            write_mapping_log("JiaoShenFile.txt", string)


def get_jiaoshen_file():
    """
    获取校审文件
    :return:
    """
    read_mapping_log("parseMuluXML.txt")


def main():
    get_jiaoshen_file()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
