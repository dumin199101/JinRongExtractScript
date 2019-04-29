# coding=utf-8
"""
@Project: JinRong
@Time: 2019/3/26 15:44
@Name: GetFirstLetter
@Author: lieyan123091
"""
import re
import sys

regex_tab = re.compile("\\t")

def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))

def multi_get_letter(str_input):
    if isinstance(str_input, unicode):
        unicode_str = str_input
    else:
        try:
            unicode_str = str_input.decode('utf8')
        except:
            try:
                unicode_str = str_input.decode('gbk')
            except:
                print 'unknown coding'
                return
    return_list = []
    for one_unicode in unicode_str:
        return_list.append(single_get_first(one_unicode))
    return return_list


def single_get_first(unicode1):
    try:
        str1 = unicode1.decode('utf-8').encode("gbk")
        ord(str1)
        return str1
    except:
        try:
            if str1[0].isalnum():
                return str1[0]
            else:
                try:
                    str1 = unicode1.decode('utf-8').encode("gbk")
                    asc = ord(str1[0]) * 256 + ord(str1[1]) - 65536
                    if asc >= -20319 and asc <= -20284:
                        return 'a'
                    if asc >= -20283 and asc <= -19776:
                        return 'b'
                    if asc >= -19775 and asc <= -19219:
                        return 'c'
                    if asc >= -19218 and asc <= -18711:
                        return 'd'
                    if asc >= -18710 and asc <= -18527:
                        return 'e'
                    if asc >= -18526 and asc <= -18240:
                        return 'f'
                    if asc >= -18239 and asc <= -17923:
                        return 'g'
                    if asc >= -17922 and asc <= -17418:
                        return 'h'
                    if asc >= -17417 and asc <= -16475:
                        return 'j'
                    if asc >= -16474 and asc <= -16213:
                        return 'k'
                    if asc >= -16212 and asc <= -15641:
                        return 'l'
                    if asc >= -15640 and asc <= -15166:
                        return 'm'
                    if asc >= -15165 and asc <= -14923:
                        return 'n'
                    if asc >= -14922 and asc <= -14915:
                        return 'o'
                    if asc >= -14914 and asc <= -14631:
                        return 'p'
                    if asc >= -14630 and asc <= -14150:
                        return 'q'
                    if asc >= -14149 and asc <= -14091:
                        return 'r'
                    if asc >= -14090 and asc <= -13119:
                        return 's'
                    if asc >= -13118 and asc <= -12839:
                        return 't'
                    if asc >= -12838 and asc <= -12557:
                        return 'w'
                    if asc >= -12556 and asc <= -11848:
                        return 'x'
                    if asc >= -11847 and asc <= -11056:
                        return 'y'
                    if asc >= -11055 and asc <= -10247:
                        return 'z'
                    return '其他'
                except:
                    return '其他'
        except:
            return '其他'

def write_mapping_log(logname, content):
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))


def get_first_letter(srcfile):
    j = 1
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            # id = info[0]
            # word = info[1].encode("utf-8").strip("\n")
            word = info[0]
            letter = single_get_first(word)
            # write_mapping_log("Baike_Word_FirstLetter.txt",id+"\t"+word+"\t"+letter.upper()+"\n")
            write_mapping_log("OrgList_FirstLetter.txt",word+"\t"+letter.upper()+"\n")
            # print j, id, word, letter.upper()
            print j,word,letter.upper()
            j = j + 1


def main():
    # a = multi_get_letter(str_input)
    # b = ''
    # for i in a:
    #     b = b + i
    # print b

    # 获取首字母：
    # srcfile = 'baike_search_word_info.txt'
    srcfile = 'org_list.txt'
    get_first_letter(srcfile)


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
