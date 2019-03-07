# coding=utf-8
"""
@Project: JinRong
@Time: 2019/3/4 11:58
@Name: GetSpecialInfoFromBookAndTitle
@Author: lieyan123091
"""
import re, sys, os

def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))

regex_tab = re.compile("\\t")
regex_line = re.compile("_")

i = 1

special_list = ["法律","公告","规定","通知","意见","政策","法规","条例","办法","规程","规则","章程","准则","试行","指引"]

def get_book(srcfile):
    global i
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            guid = info[0]
            bookname = info[1].strip("\n")
            for word in special_list:
                if bookname.find(word) > -1:
                    print i,guid,bookname,word
                    write_mapping_log("get_bookname.txt",guid+"\t"+bookname+"\t"+word+"\n")
                    i = i + 1
                    break




def get_title(srcfile):
    global i
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            guid = info[0]
            bookid = info[1]
            title = info[2]
            startpage = info[3]
            endpage = info[4]
            relation_key = info[5].strip("\n")
            info2 = regex_line.split(relation_key)
            bookname = info2[0]
            tree = info2[1]
            for word in special_list:
                if title.find(word) > -1:
                    print i,guid,bookid,bookname,tree,title,word
                    write_mapping_log("get_title.txt", guid + "\t" + bookid + "\t" + bookname + "\t" + title + "\t" + startpage + "\t" + endpage + "\t" + word + "\n")
                    i = i + 1
                    break












def main():
    # srcfile = u"bookname.txt"
    # get_book(srcfile)

    srcfile = u"title.txt"
    get_title(srcfile)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
