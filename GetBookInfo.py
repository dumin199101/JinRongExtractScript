# coding=utf-8
import os
import sys
from bs4 import BeautifulSoup
import re


ROOTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))

def del_blank_char(str):
    """
    去除字符串中的空白跟换行符
    :param str:
    :return:
    """
    rep = re.compile(r'(\n|\t)')
    (fstr, count) = rep.subn('', str)
    return fstr

def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))




def get_book_info(file):
    soup = BeautifulSoup(open(file.encode("gbk")),features='xml')

    (filepath, name) = os.path.split(file)
    (shotname,extension) = os.path.splitext(name)

    dict = []
    info = ''

    # title信息
    titles = soup.find_all("title")
    for title in titles:
        for tag in title.parents:
            dict.append(tag.name)
        # 排除封面title
        if 'cover' not in dict:
            # 排除seriesTitle缺失的情况
            if len(titles)==2:
                info = info + "暂无" + "\t"
                # title = title.string
                title = shotname
                info = info  + title + "\t"
            else:
                if title.has_attr('role'):
                    seriestitle = title.string
                    info = info  + seriestitle + "\t"
                else:
                    # title = title.string
                    title = shotname
                    info = info + title + "\t"
        # 重置列表
        dict = []

    # ISBN、CIP、印次信息
    isbn = soup.select('biblioid[class="isbn"]')[0].get_text()
    yinci = soup.select('biblioid[otherclass="yinci"]')[0].get_text()
    cip = soup.select('biblioid[otherclass="cip"]')[0].get_text()
    info = info + isbn + "\t" + cip + "\t" + yinci + "\t"

    # 作者、编者信息
    authors = soup.find_all("author")
    author_list = []
    for author in authors:
        author_list.append(author.personname.string)
    author_info = ",".join(author_list)

    editors = soup.find_all("editor")
    editor_list = []
    if len(editors) > 0:
        for editor in editors:
            editor_list.append(editor.personname.string)
        editor_info = ",".join(editor_list)
    else:
        editor_info = '暂无'

    info = info + author_info + "\t" + editor_info + "\t"

    # 出版社信息
    publishers = soup.find_all("publisher")
    publisher_list = []
    for publisher in publishers:
        publisher_list.append(publisher.publishername.string)
    publisher_info = ",".join(publisher_list)
    info = info + publisher_info + "\t"

    # 图书在版编目(CIP)数据
    if len(soup.select('releaseinfo[role="CIP"]'))>0:
        CIP_info = soup.select('releaseinfo[role="CIP"]')[0].get_text()
        CIP_info = del_blank_char(CIP_info)
    else:
        CIP_info = "暂无"


    # 价格、语言、字数、印张、装订格式
    price = soup.select('releaseinfo[role="price"]')[0].get_text()
    language = soup.select('releaseinfo[role="language"]')[0].get_text()
    if len(soup.select('releaseinfo[role="wordnum"]'))>0:
        wordnum = soup.select('releaseinfo[role="wordnum"]')[0].get_text()
        wordnum = int(wordnum) * 1000
    else:
        wordnum = 0
    if len(soup.select('releaseinfo[role="sheets"]'))>0:
        sheets = soup.select('releaseinfo[role="sheets"]')[0].get_text()
    else:
        sheets = '0'
    bindingformat = soup.select('releaseinfo[role="bindingformat "]')[0].get_text()

    info = info + price + "\t" + language + "\t" + str(wordnum) + "\t" + sheets + "\t" + bindingformat + "\t"

    # 关键词
    keywords = soup.keywordset.stripped_strings
    key = ''
    for keyword in keywords:
        key = key + keyword

    info = info + key + "\t"

    # 出版时间 版次：
    revnumber = soup.revhistory.revision.revnumber.string
    date = soup.revhistory.revision.date.string

    info = info + revnumber + "\t" + date + "\t"

    # PDF页数：
    pages = soup.select('pagenums[role="pdfpage"]')[0].get_text()

    info = info + pages + "\t"  + CIP_info + "\n"

    write_mapping_log("BookInfo.txt",info)

def main():
    # 配置数据
    srcdir = u'E:\Goosuu\JinRong\Script\Deal-Middle\BOOKINFO_XML\第一批数据'
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir, filename)
        get_book_info(file)
        print filename



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()