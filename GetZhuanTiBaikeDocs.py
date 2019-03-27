# coding=utf-8
"""
@Project: JinRong
@Time: 2019/3/27 10:36
@Name: GetZhuanTiBaikeDocs
@Author: lieyan123091
@Desc: 批量抓取百科详情页信息
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


def get_doc_list(id, name, link):
    """
    获取金融百科词条详情信息
    :param id: 词条ID
    :param name: 词条名称
    :param link: 词条链接
    :return:
    """
    # 构建请求头，为防止超时，每页构建一次
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "__cfduid=d280bdec1bdb266a2ac1d95851e93109d1553223481; PHPSESSID=i43rdu7ikbvbmu7lenm66a9lu0; hd_sid=HUcYSD; hd_searchtime=1553246649; Hm_lvt_271cf5a817c4c9b535ad4e989d360599=1553223241; Hm_lpvt_271cf5a817c4c9b535ad4e989d360599=1553652218; Hm_lvt_3470dc9e83304dd22bcf5f49af714476=1553223243; Hm_lpvt_3470dc9e83304dd22bcf5f49af714476=1553652218",
        "Host": "www.jinrongbaike.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    url = "http://www.jinrongbaike.com/" + link
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html, features='lxml')

    # 业务逻辑代码

    content_body = soup.find(id="content-body")
    if content_body is not None:
        # 去除CSS链接
        content_body.find('link').extract()
        # 去除图片标签
        img_list = content_body.find_all("img")
        for img_tag in img_list:
            img_tag.extract()

        # 去除a标签链接
        a_list = content_body.find_all("a")
        for a_tag in a_list:
            a_tag['href'] = 'javascript:void(0);'
    else:
        content_body = '<p>该词条待审核通过</p>'

    write_mapping_log("Baike_Word_Docs.txt",id+"\t"+name+"\t"+link+"\t"+del_blank_char(str(content_body))+"\n")
    response.close()


def get_docs(srcfile):
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
            id = info[0]
            name = info[1]
            link = info[2].strip("\n")
            get_doc_list(id, name, link)
            print i, name, link
            i = i + 1

def test_get_doc(link):
    # 构建请求头，为防止超时，每页构建一次
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "__cfduid=d280bdec1bdb266a2ac1d95851e93109d1553223481; PHPSESSID=i43rdu7ikbvbmu7lenm66a9lu0; hd_sid=HUcYSD; hd_searchtime=1553246649; Hm_lvt_271cf5a817c4c9b535ad4e989d360599=1553223241; Hm_lpvt_271cf5a817c4c9b535ad4e989d360599=1553652218; Hm_lvt_3470dc9e83304dd22bcf5f49af714476=1553223243; Hm_lpvt_3470dc9e83304dd22bcf5f49af714476=1553652218",
        "Host": "www.jinrongbaike.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    url = "http://www.jinrongbaike.com/" + link
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html, features='lxml')
    # print soup.prettify()
    content_body = soup.find(id="content-body")
    print content_body
    # # 去除CSS链接
    # content_body.find('link').extract()
    # # 去除图片标签
    # img_list = content_body.find_all("div",class_="img")
    # for img_tag in img_list:
    #     img_tag.extract()
    # # 去除a标签链接
    # a_list = content_body.find_all("a",class_="innerlink")
    # for a_tag in a_list:
    #     a_tag['href'] = 'javascript:void(0);'
    # print content_body




def main():
    # 批量获取词条信息
    srcfile = u"baike_search_word_info.txt"
    get_docs(srcfile)

    # 测试抓取单个词条
    # link = "doc-view-48306.htm"
    # test_get_doc(link)





if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
