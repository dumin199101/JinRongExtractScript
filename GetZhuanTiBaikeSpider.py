# coding=utf-8
"""
@Project: JinRong
@Time: 2019/3/21 18:03
@Name: GetZhuanTiBaikeSpider
@Author: lieyan123091
抓取百度百科金融词条
1.构建调度器
2.构建URL管理器
3.构建HTML下载器
4.构建HTML解析器
5.保存文本信息
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


def get_category_info():
    """
    获取金融百科分类信息
    :return:
    """
    # 构建请求头
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "__cfduid=d280bdec1bdb266a2ac1d95851e93109d1553223481; PHPSESSID=i43rdu7ikbvbmu7lenm66a9lu0; hd_sid=HUcYSD; hd_searchtime=1553224894; Hm_lvt_271cf5a817c4c9b535ad4e989d360599=1553223241; Hm_lpvt_271cf5a817c4c9b535ad4e989d360599=1553224772; Hm_lvt_3470dc9e83304dd22bcf5f49af714476=1553223243; Hm_lpvt_3470dc9e83304dd22bcf5f49af714476=1553224772",
        "Host": "www.jinrongbaike.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    url = "http://www.jinrongbaike.com/index.php?category"
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html, features='lxml')
    # print soup.prettify()
    # 获取一级分类
    dl_list = soup.select("section.wrap > #category > dl.f14")
    for dl in dl_list:
        dt = dl.find("dt")
        dd_list = dl.find_all("dd")
        dt_a = dt.find('a')
        dt_href = dt_a.get("href")
        dt_name = dt_a.string
        dt_id = re_digit.search(dt_href).group()
        print "*" * 20,dt_id,dt_name,dt_href,'顶级分类'
        write_mapping_log("Baike_Category.txt", dt_id + "\t" + dt_name + "\t" + dt_href + "\t" + '顶级分类' + "\t" + "0" + "\n")
        for dd in dd_list:
            dd_a = dd.find('a')
            dd_href = dd_a.get("href")
            dd_name = dd_a.string
            dd_id = re_digit.search(dd_href).group()
            print "*" * 30,dd_id,dd_name,dd_href,dt_name
            write_mapping_log("Baike_Category.txt",dd_id+"\t"+dd_name+"\t"+dd_href+"\t"+dt_name+"\t"+dt_id+"\n")


def get_page_num(srcfile):
    """
    获取列表总页码，计算分页数值
    :return:
    """
    with open(srcfile, "r") as f1:
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            # 为防止超时，每次进来创建一次
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.8",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Cookie": "__cfduid=d280bdec1bdb266a2ac1d95851e93109d1553223481; PHPSESSID=i43rdu7ikbvbmu7lenm66a9lu0; hd_sid=HUcYSD; hd_searchtime=1553224894; Hm_lvt_271cf5a817c4c9b535ad4e989d360599=1553223241; Hm_lpvt_271cf5a817c4c9b535ad4e989d360599=1553224772; Hm_lvt_3470dc9e83304dd22bcf5f49af714476=1553223243; Hm_lpvt_3470dc9e83304dd22bcf5f49af714476=1553224772",
                "Host": "www.jinrongbaike.com",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
            }
            info = regex_tab.split(line)
            url = "http://www.jinrongbaike.com/" + info[2]
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            html = response.read()
            soup = BeautifulSoup(html, features='lxml')
            # print info[1],soup.select("#fenye > span.gray")
            if len(soup.select("#fenye > span.gray")) == 0:
                # 说明只有不到一页数据，未产生分页：
                strs = soup.select("section.wrap > .group1 > h2 > span")[0]
                for string in strs.strings:
                    if string.find('创建该分类下的词条') < 0:
                        # print info[1],re_digit.search(string).group()
                        total = re_digit.search(string).group()
            else:
                total = re_digit.search(soup.select("#fenye > span.gray")[0].string).group()
            print info[1],info[2],total
            write_mapping_log("Baike_Category_Pages.txt",info[1]+"\t"+info[2]+"\t"+str(total)+"\n")



def get_word_list(link,total,name):
    """
    获取金融百科对应分类下的词条列表
    :return:
    """
    total = int(total)
    if total > 0 :
        # 将来这个地方变成动态参数
        if (total % 10) == 0:
            endpage =  int(total / 10)
        else:
            endpage = int(total / 10) + 1
        j = 1
        for i in range(1,endpage+1):
            # 构建请求头，为防止超时，每页构建一次
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.8",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Cookie": "__cfduid=d280bdec1bdb266a2ac1d95851e93109d1553223481; PHPSESSID=i43rdu7ikbvbmu7lenm66a9lu0; hd_sid=HUcYSD; hd_searchtime=1553224894; Hm_lvt_271cf5a817c4c9b535ad4e989d360599=1553223241; Hm_lpvt_271cf5a817c4c9b535ad4e989d360599=1553224772; Hm_lvt_3470dc9e83304dd22bcf5f49af714476=1553223243; Hm_lpvt_3470dc9e83304dd22bcf5f49af714476=1553224772",
                "Host": "www.jinrongbaike.com",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
            }
            url = "http://www.jinrongbaike.com/"+link[:-4]+"-" + str(i) +".htm"
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            html = response.read()
            soup = BeautifulSoup(html, features='lxml')
            # print soup.prettify()
            dl_list = soup.select("section.wrap dl.col-dl")
            for dl in dl_list:
                # 获取标题
                dt = dl.find("dt")
                dt_a = dt.find('a')
                dt_href = dt_a.get("href")
                dt_name = dt_a.string
                dt_id = re_digit.search(dt_href).group()
                # print "*" * 20, dt_id, dt_name, dt_href
                # 获取摘要
                # dd_list = dl.find_all("dd",class_="gray")
                # dd_abstract = dd_list[1]
                # for string in dd_abstract.stripped_strings:
                #     if string.find('[阅读全文:]') < 0:
                #         abstract = del_blank_char(string)[3:].replace("&nbsp;","").replace("　","")
                if dt_name is not None:
                    # 排除乱码情况
                    write_mapping_log("Baike_Words.txt",dt_id+"\t"+dt_name+"\t"+dt_href+"\t"+name+"\t"+str(i)+"\t"+link+"\n")
                    print j,dt_id, dt_name, dt_href,name
                j = j + 1



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
            name = info[0]
            link = info[1]
            total = info[2]
            print i,name
            get_word_list(link,total,name)
            i = i + 1












def main():
    # 1.获取分类信息
    # get_category_info()

    # 2.获取记录数
    # srcfile = u"Baike_Category.txt"
    # get_page_num(srcfile)

    # 3.获取词条信息
    srcfile = u"Baike_Category_Pages.txt"
    get_words(srcfile)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
