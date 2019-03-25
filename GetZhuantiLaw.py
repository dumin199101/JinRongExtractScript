# coding=utf-8
"""
@Project: JinRong
@Time: 2019/3/20 16:25
@Name: GetZhuantiLaw
@Author: lieyan123091
"""
import re, sys,time

def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))

regex_tab = re.compile("\\t")
regex_blank = re.compile(" ")

i = 1

def get_info(srcfile):
    global i
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            # print i,len(info)
            # i = i + 1
            guid = info[0]
            title = info[3]
            hangye = info[8]
            jigou = info[9]
            shishi = info[10]
            pubdate = info[11]
            shishidate = info[15].strip("\n")
            # 行业信息
            hangye_info = regex_blank.split(hangye)
            if len(hangye_info) > 1:
                hangye_list = []
                for str in hangye_info:
                    hangye_list.append(str)
                hangye_info = ",".join(hangye_list)
            else:
                hangye_info = hangye
            #机构信息
            jigou_info = regex_blank.split(jigou)
            if len(jigou_info) > 1:
                jigou_list = []
                for str in jigou_info:
                    jigou_list.append(str)
                jigou_info = ",".join(jigou_list)
            else:
                jigou_info = jigou
                # print guid,jigou_info
            # 实施单位
            shishi_info = regex_blank.split(shishi)
            if len(shishi_info) > 1:
                shishi_list = []
                for str in shishi_info:
                    shishi_list.append(str)
                shishi_info = ",".join(shishi_list)
            else:
                shishi_info = shishi
                # print guid, shishi_info
            # 发布时间
            pubyear = pubdate[:4]
            pubdate = pubdate.replace("/","-")
            pubdate = time.strftime("%Y-%m-%d", time.localtime(time.mktime(time.strptime(pubdate, "%Y-%m-%d"))))
            # 实施时间
            shishidate = shishidate.replace("/", "-")
            shishidate = time.strftime("%Y-%m-%d", time.localtime(time.mktime(time.strptime(shishidate, "%Y-%m-%d"))))

            write_mapping_log("law_title.txt",guid+"\t"+info[1]+"\t"+info[2]+"\t"+title+"\t"+info[4]+"\t"+info[5]+"\t"+info[6]+"\t"+info[7]+"\t"+hangye_info+"\t"+jigou_info+"\t"+shishi_info+"\t"+pubdate+"\t"+info[12]+"\t"+info[13]+"\t"+info[14]+"\t"+shishidate+"\t"+pubyear+"\n")
            print i,guid
            i = i + 1


def get_book_info(srcfile):
    global i
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            # print i,len(info)
            # i = i + 1
            guid = info[0]
            book = info[1]
            hangye = info[6]
            jigou = info[7]
            shishi = info[8]
            pubdate = info[9]
            shishidate = info[13]
            link = info[14].strip("\n")
            # 行业信息
            hangye_info = regex_blank.split(hangye)
            if len(hangye_info) > 1:
                hangye_list = []
                for str in hangye_info:
                    hangye_list.append(str)
                hangye_info = ",".join(hangye_list)
            else:
                hangye_info = hangye
            #机构信息
            jigou_info = regex_blank.split(jigou)
            if len(jigou_info) > 1:
                jigou_list = []
                for str in jigou_info:
                    jigou_list.append(str)
                jigou_info = ",".join(jigou_list)
            else:
                jigou_info = jigou
                # print guid,jigou_info
            # 实施单位
            shishi_info = regex_blank.split(shishi)
            if len(shishi_info) > 1:
                shishi_list = []
                for str in shishi_info:
                    shishi_list.append(str)
                shishi_info = ",".join(shishi_list)
            else:
                shishi_info = shishi
                # print guid, shishi_info
            # 发布时间
            pubyear = pubdate[:4]
            pubdate = pubdate.replace("/","-")
            pubdate = time.strftime("%Y-%m-%d", time.localtime(time.mktime(time.strptime(pubdate, "%Y-%m-%d"))))
            # 实施时间
            shishidate = shishidate.replace("/", "-")
            shishidate = time.strftime("%Y-%m-%d", time.localtime(time.mktime(time.strptime(shishidate, "%Y-%m-%d"))))
            write_mapping_log("law_book_info_guid.txt",guid+"\t"+book+"\t"+info[2]+"\t"+info[3]+"\t"+info[4]+"\t"+info[5]+"\t"+hangye_info+"\t"+jigou_info+"\t"+shishi_info+"\t"+pubdate+"\t"+info[10]+"\t"+info[11]+"\t"+info[12]+"\t"+shishidate+"\t"+pubyear+"\t"+link+"\n")
            print i,guid
            i = i + 1





def main():
    srcfile = u"Law_Book_Info.txt"
    get_book_info(srcfile)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()