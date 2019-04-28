# coding=utf-8
"""
@Project: JinRong
@Time: 2019/4/28 10:00
@Name: GetOrgInfo
@Author: lieyan123091
@Desc: 获取机构详情
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


def get_doc_list(name, link):
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
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "BAIDUID=0F2569A1C342D94E36681DAEFCB97FEB:FG=1; pgv_pvi=837474304; pgv_si=s7368010752; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1556417012; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1556418021",
        "Host": "baike.baidu.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    }
    url = link
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html, features='lxml')

    # 业务逻辑代码
    content_body = soup.find(class_="main-content")
    # ①去除特色词条标识
    if content_body.find('a', class_="excellent-icon") is not None:
        content_body.find('a', class_="excellent-icon").extract()
    # ②去掉顶部工具栏
    if content_body.find('div', class_="top-tool") is not None:
        content_body.find('div', class_="top-tool").extract()
    # ③去掉锁定图标
    if content_body.find('a', class_="lock-lemma") is not None:
        content_body.find('a', class_="lock-lemma").extract()
    # ④去掉讨论图标
    if content_body.find('a', class_="lemma-discussion") is not None:
        content_body.find('a', class_="lemma-discussion").extract()
    # ⑤去除图片标签
    img_list = content_body.find_all("a", class_="image-link")
    for img_tag in img_list:
        img_tag['href'] = 'javascript:void(0);'
        img_tag['target'] = '_self'
        img_tag.find("img")['src'] = img_tag.find("img")['data-src']
        img_tag.find("img")['data-src'] = ''
        img_tag.find("img")['class'] = ''
    img_list_1 = content_body.find_all("a", class_="lemma-album")
    for img_tag in img_list_1:
        img_tag['href'] = 'javascript:void(0);'
        img_tag['target'] = '_self'

    # ⑥去除a标签链接
    a_list = content_body.find_all("a")
    for a_tag in a_list:
        a_tag['href'] = 'javascript:void(0);'
        a_tag['target'] = '_self'
    # ⑦去除词条图册：
    if content_body.find('div', class_="album-list") is not None:
        content_body.find('div', class_="album-list").extract()
    # ⑧去除图说，参考文献，标签
    if content_body.find('div', class_="tashuo-bottom") is not None:
        content_body.find('div', class_="tashuo-bottom").extract()
    if content_body.find('dl', class_="lemma-reference") is not None:
        content_body.find('dl', class_="lemma-reference").extract()
    if content_body.find('div', id="open-tag") is not None:
        content_body.find('div', id="open-tag").extract()
    if content_body.find('a', class_="edit-lemma") is not None:
        content_body.find('a', class_="edit-lemma").extract()
    if content_body.find('a', class_="edit-icon") is not None:
        content_body.find('a', class_="edit-icon").extract()
    if content_body.find('iframe') is not None:
        content_body.find('iframe').extract()

    # 获取简介
    summary = ''
    sumamrty_tag = soup.find(class_="lemma-summary")
    for string in sumamrty_tag.stripped_strings:
        summary = summary + string

    print summary
    write_mapping_log("Org_Details.txt",name+"\t"+summary+"\t"+del_blank_char(str(content_body))+"\n")
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
            name = info[0]
            link = info[1].strip("\n")
            get_doc_list(name, link)
            print i, name
            i = i + 1




def test_get_doc(link):
    # 构建请求头，为防止超时，每页构建一次
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "BAIDUID=0F2569A1C342D94E36681DAEFCB97FEB:FG=1; pgv_pvi=837474304; pgv_si=s7368010752; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1556417012; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1556418021",
        "Host": "baike.baidu.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    }
    url = link
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html, features='lxml')
    # print soup.prettify()
    content_body = soup.find(class_="main-content")
    # print content_body.prettify()
    # ①去除特色词条标识
    if content_body.find('a',class_="excellent-icon") is not None:
        content_body.find('a',class_="excellent-icon").extract()
    # ②去掉顶部工具栏
    if content_body.find('div', class_="top-tool") is not None:
        content_body.find('div', class_="top-tool").extract()
    # ③去掉锁定图标
    if content_body.find('a', class_="lock-lemma") is not None:
        content_body.find('a', class_="lock-lemma").extract()
    # ④去掉讨论图标
    if content_body.find('a', class_="lemma-discussion") is not None:
        content_body.find('a', class_="lemma-discussion").extract()
    # ⑤去除图片标签
    img_list = content_body.find_all("a",class_="image-link")
    # img_list = content_body.find_all("div",class_="lemma-picture")
    for img_tag in img_list:
        # img_tag.extract()
        img_tag['href'] = 'javascript:void(0);'
        img_tag['target'] = '_self'
        img_tag.find("img")['src'] = img_tag.find("img")['data-src']
        img_tag.find("img")['data-src'] = ''
        img_tag.find("img")['class'] = ''
    img_list_1 = content_body.find_all("a", class_="lemma-album")
    for img_tag in img_list_1:
        # img_tag.extract()
        img_tag['href'] = 'javascript:void(0);'
        img_tag['target'] = '_self'

    # ⑥去除a标签链接
    a_list = content_body.find_all("a")
    for a_tag in a_list:
        a_tag['href'] = 'javascript:void(0);'
        a_tag['target'] = '_self'
    # ⑦去除词条图册：
    if content_body.find('div', class_="album-list") is not None:
        content_body.find('div', class_="album-list").extract()
    # ⑧去除图说，参考文献，标签
    if content_body.find('div', class_="tashuo-bottom") is not None:
        content_body.find('div', class_="tashuo-bottom").extract()
    if content_body.find('dl', class_="lemma-reference") is not None:
        content_body.find('dl', class_="lemma-reference").extract()
    if content_body.find('div', id="open-tag") is not None:
        content_body.find('div', id="open-tag").extract()
    if content_body.find('a', class_="edit-lemma") is not None:
        content_body.find('a', class_="edit-lemma").extract()
    if content_body.find('a', class_="edit-icon") is not None:
        content_body.find('a', class_="edit-icon").extract()
    if content_body.find('iframe') is not None:
        content_body.find('iframe').extract()
    print content_body.prettify()

    # 获取简介
    summary = ''
    sumamrty_tag = soup.find(class_="lemma-summary")
    print sumamrty_tag
    for string in sumamrty_tag.stripped_strings:
        summary = summary + string
    print del_blank_char(summary)





def main():
    # 批量获取词条信息
    srcfile = u"org_list.txt"
    get_docs(srcfile)

    # 测试抓取单个词条
    # link = "https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E4%BA%BA%E6%B0%91%E9%93%B6%E8%A1%8C/418386?fr=aladdin"
    # link = "https://baike.baidu.com/item/%E8%81%94%E6%B3%B0%E5%A4%A7%E9%83%BD%E4%BC%9A%E4%BA%BA%E5%AF%BF%E4%BF%9D%E9%99%A9%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8/6411684?fr=aladdin"
    # link = "https://baike.baidu.com/item/%E5%B9%B3%E5%AE%89%E9%93%B6%E8%A1%8C/10609311?fr=aladdin"
    # link = "https://baike.baidu.com/item/%E6%B7%B1%E5%9C%B3%E5%B8%82%E5%B0%8F%E8%B5%A2%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8"
    # test_get_doc(link)





if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()

