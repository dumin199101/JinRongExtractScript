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
    根据MULU_File.txt计算目录层级，得出下级目录的上级目录名称，并形成参照文件MULU_Level_File.txt
    :param logname:
    :return:
    """
    with open(logname,"r") as f1:
        regex_tab = re.compile("\\t")
        max_level = 1
        while True:
            line = f1.readline().decode("utf-8")
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            """
            str = info[0] + "\t" + info[1] + "\t" + info[5] + "\t" + info[6] + "\t" + info[7]
            write_mapping_log("Level.txt",str)
          """
            # 先检测最大层级数
            level = int(info[6])
            if max_level < level:
                max_level = level
        print "当前文件最大层级数：",max_level
        if max_level>4:
            print "最大层级数超过限定值4，请注意调整程序..."
            return False
    with open(logname, "r") as f1:
        regex_tab = re.compile("\\t")
        while True:
            line = f1.readline().decode("utf-8")
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            global ChapterName,ChapterName2,ChapterName3
            level = int(info[6])
            if level==1:
                ChapterName = info[0]
                str = info[0] + "\t" + info[1] + "\t" + info[1] + "\n"
            elif level==2:
                str = info[0] + "\t" + info[1] + "\t" + ChapterName + "\n"
                ChapterName2 = info[0]
            elif level==3:
                str = info[0] +  "\t" + info[1] + "\t" +ChapterName2 + "\n"
                ChapterName3 = info[0]
            elif level==4:
                str = info[0] + "\t" + info[1] + "\t" +ChapterName3 + "\n"
            # print str
            write_mapping_log("MULU_Level_File.txt",str)










def get_level_name():
    read_mapping_log("parseMuluXML.txt")



def main():
  get_level_name()



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()