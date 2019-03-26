# coding=utf-8
"""
@Project: JinRong
@Time: 2019/3/26 15:52
@Name: GetZhuanTiBaikeHotWords
@Author: lieyan123091
"""
import sys
import urllib
import urllib2
from bs4 import BeautifulSoup
import re

re_digit = re.compile(r"\d+")
regex_tab = re.compile(r"\t")


def del_blank_char(str):
    """
    去除字符串中的空白跟换行符
    :param str:
    :return:
    """
    rep = re.compile(r'(\n|\t|\r)')
    (fstr, count) = rep.subn('', str)
    return fstr


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))


def get_word_list(link, total,type):
    """
    获取金融百科对应分类下的词条列表
    :return:
    """
    total = int(total)
    if total > 0:
        # 将来这个地方变成动态参数
        if (total % 10) == 0:
            endpage = int(total / 10)
        else:
            endpage = int(total / 10) + 1
        for i in range(1, endpage + 1):
            # 构建请求头，为防止超时，每页构建一次
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.8",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Cookie": "_cfduid=d280bdec1bdb266a2ac1d95851e93109d1553223481; PHPSESSID=i43rdu7ikbvbmu7lenm66a9lu0; hd_sid=HUcYSD; hd_searchtime=1553246649; Hm_lvt_271cf5a817c4c9b535ad4e989d360599=1553223241; Hm_lpvt_271cf5a817c4c9b535ad4e989d360599=1553252991; Hm_lvt_3470dc9e83304dd22bcf5f49af714476=1553223243; Hm_lpvt_3470dc9e83304dd22bcf5f49af714476=1553252991",
                "Host": "www.jinrongbaike.com",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
            }
            url = "http://www.jinrongbaike.com/" + link + "-" + str(i) + ".htm"
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            html = response.read()
            soup = BeautifulSoup(html, features='lxml')
            # print soup.prettify()
            dl_list = soup.select("section.wrap dl.col-dl")
            for dl in dl_list:
                # 获取标题
                dd_list = dl.find_all("dd")
                for dd in dd_list:
                    dd_a = dd.find('a')
                    dd_href = dd_a.get("href")
                    dd_name = dd_a.string
                    dd_id = re_digit.search(dd_href).group()
                    print dd_name,dd_id,dd_href,type,i
                    write_mapping_log("Baike_Hot_Word.txt",dd_id+"\t"+dd_name+"\t"+dd_href+"\t"+type+"\t"+str(i)+"\n")
            response.close()


def get_words(srcfile):
    """
    批量获取词条
    :param srcfile:
    :return:
    """
    with open(srcfile, "r") as f1:
        i = 1
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            link = info[0]
            total = info[1]
            type = info[2].strip("\n")
            get_word_list(link, total, type)
            i = i + 1





def main():
    # 获取词条信息
    srcfile = u"Baike_Hot.txt"
    get_words(srcfile)




if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()



