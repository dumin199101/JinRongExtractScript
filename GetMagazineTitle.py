# coding=utf-8
"""
@Project: JinRong
@Time: 2018/12/24 17:35
@Name: GetMagazineTitle
@Author: lieyan123091
提取期刊期刊信息、标题信息、全文信息、
"""

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
    rep = re.compile(r'(\n|\t|\s+)')
    (fstr, count) = rep.subn('', str)
    return fstr


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))


def get_magazine_title(file):
    (filepath, name) = os.path.split(file)
    (bookname, extension) = os.path.splitext(name)

    soup = BeautifulSoup(open(file.encode("gbk")), features='xml')

    # 第①部分信息：magazineId,magzineName,magzineYear,magzineOrder,banbie,cover,file
    magazineId = soup.select('magzineId')[0].get_text()
    magzineName = soup.select('magzineName')[0].get_text()
    magzineYear = soup.select('magzineYear')[0].get_text()
    magzineOrder = soup.select('magzineOrder')[0].get_text()
    banbie = soup.select('banbie')[0].get_text()
    if banbie == '':
        banbie = '信息不详'
    cover = soup.select('cover')[0].get_text()
    file = soup.select('file')[0].get_text()
    print bookname, magazineId, magzineName, magzineYear, magzineOrder, banbie, cover, file
    # info = bookname + "\t" + magazineId + "\t" + magzineName + "\t" + magzineYear + "\t" + magzineOrder + "\t" + banbie + "\t" + cover + "\t" + file + "\n"
    # write_mapping_log("MagazineInfo.txt",info)


    # # 第②部分信息：magazineforum,magazinecolumns,magazinecolumn
    magazineforums = soup.select("magazineforum")
    # 一级标签获取
    for chapter in magazineforums:
        name_tag = chapter.find('name')
        if name_tag.string is None or name_tag.string.strip() == '':
            magazinecolumn_tags = chapter.magazinecolumns.find_all('magazinecolumn')
            for magazinecolumn_tag in magazinecolumn_tags:
                # 去除空白字符
                # print "*" * 10, del_blank_char(magazinecolumn_tag.find('name').string)
                # 获取二级标签
                docs_tag = magazinecolumn_tag.docs.find_all('doc')
                for doc_tag in docs_tag:
                    id = doc_tag.id.string
                    title = doc_tag.front.title.string
                    if title is None:
                        title = ''
                        for string in doc_tag.front.title.strings:
                            title = title + string
                    subtitle = doc_tag.front.subTitle.string
                    if subtitle is None:
                        subtitle = '暂无'
                    englishtitle = doc_tag.front.EnglishTitle.string
                    if englishtitle is None:
                        englishtitle = '暂无'
                    englishsubtitle = doc_tag.front.EnglishSubTitle.string
                    if englishsubtitle is None:
                        englishsubtitle = '暂无'
                    person_list = []
                    persons = doc_tag.front.persons
                    for person in persons:
                        # 排除空白跟换行对象
                        if person.name is None:
                            continue
                        if person.find('name').string is not None:
                            person_list.append(person.find('name').string)
                    person_info = ','.join(person_list)
                    keywords = doc_tag.front.keywords
                    key = '暂无关键词'
                    key_list = []
                    if len(keywords.find_all('keyword')) > 0:
                        key = ''
                        for keyword in keywords:
                            if keyword.string is None:
                                continue
                            if len(keyword.string) > 1:
                                key_list.append(keyword.string)
                                key = ",".join(key_list)
                    keywordens = doc_tag.front.keywordEns
                    key_ens = '暂无英文关键词'
                    key_en_list = []
                    if len(keywordens.find_all('keywordEn')) > 0:
                        key_ens = ''
                        for keyword_en in keywordens:
                            if keyword_en.string is None:
                                continue
                            if len(keyword_en.string) > 1:
                                key_en_list.append(keyword_en.string)
                                key_ens = ",".join(key_en_list)
                    abstract = doc_tag.front.abstract.string
                    if abstract is None:
                        abstract = '暂无'
                    enabstract = doc_tag.find('en-abstract').string
                    if enabstract is None:
                        enabstract = '暂无'
                    fund = doc_tag.front.fund.string
                    if fund is None:
                        fund = '暂无'
                    issue = doc_tag.front.issue.string
                    if issue is None:
                        issue = '暂无'
                    issueNo = doc_tag.front.issueNo.string
                    if issueNo is None:
                        issueNo = '暂无'
                    pageRange = doc_tag.content.find(role="pdfpage").string
                    pages = doc_tag.front.pages.string
                    # print "*" * 20, bookname,id, title, subtitle, englishtitle, englishsubtitle, person_info, key, key_ens, abstract, enabstract, fund, issue, issueNo, pageRange, pages
                    # info = bookname + "_" + id + "_" + title + "\t" + bookname + "_" + id + "\t" + bookname + "\t" + id + "\t" + title + "\t" + subtitle + "\t" + englishtitle + "\t" + englishsubtitle + "\t" + person_info + "\t" + key + "\t" + key_ens + "\t" + abstract + "\t" + enabstract + "\t" + fund + "\t" + issue + "\t" + issueNo + "\t" + pageRange + "\t" + pages + "\n"
                    # write_mapping_log("MagazineTitle.txt", info)
                    # 第三部分获取正文信息：
                    content_file = doc_tag.content.file.string
                    print content_file
                    content = ''
                    for tag in doc_tag.content.find_all(True):
                        if tag.name == 'para':
                            if tag.string is not None:
                                content = content + tag.string
                            else:
                                for string in tag.strings:
                                    content = content + string
                    info = bookname + "_" + id + "_" + title + "\t" + bookname + "\t" + id + "\t" + title + "\t" + del_blank_char(content) + "\n"
                    write_mapping_log("MagazineContent.txt", info)
        else:
            # print "*" * 10, del_blank_char(name_tag.string)
            # 获取二级标签
            magazinecolumn_tags = chapter.magazinecolumns.find_all('magazinecolumn')
            for magazinecolumn_tag in magazinecolumn_tags:
                # print "*" * 20, del_blank_char(magazinecolumn_tag.find('name').string)
                # 获取三级标签
                docs_tag = magazinecolumn_tag.docs.find_all('doc')
                for doc_tag in docs_tag:
                    id = doc_tag.id.string
                    title = doc_tag.front.title.string
                    if title is None:
                        title = ''
                        for string in doc_tag.front.title.strings:
                            title = title + string
                    subtitle = doc_tag.front.subTitle.string
                    if subtitle is None:
                        subtitle = '暂无'
                    englishtitle = doc_tag.front.EnglishTitle.string
                    if englishtitle is None:
                        englishtitle = '暂无'
                    englishsubtitle = doc_tag.front.EnglishSubTitle.string
                    if englishsubtitle is None:
                        englishsubtitle = '暂无'
                    person_list = []
                    persons = doc_tag.front.persons
                    for person in persons:
                        # 排除空白跟换行对象
                        if person.name is None:
                            continue
                        if person.find('name').string is not None:
                            person_list.append(person.find('name').string)
                    person_info = ','.join(person_list)
                    keywords = doc_tag.front.keywords
                    key = '暂无关键词'
                    key_list = []
                    if len(keywords.find_all('keyword')) > 0:
                        key = ''
                        for keyword in keywords:
                            if keyword.string is None:
                                continue
                            if len(keyword.string) > 1:
                                key_list.append(keyword.string)
                                key = ",".join(key_list)
                    keywordens = doc_tag.front.keywordEns
                    key_ens = '暂无英文关键词'
                    key_en_list = []
                    if len(keywordens.find_all('keywordEn')) > 0:
                        key_ens = ''
                        for keyword_en in keywordens:
                            if keyword_en.string is None:
                                continue
                            if len(keyword_en.string) > 1:
                                key_en_list.append(keyword_en.string)
                                key_ens = ",".join(key_en_list)
                    abstract = doc_tag.front.abstract.string
                    if abstract is None:
                        abstract = '暂无'
                    enabstract = doc_tag.find('en-abstract').string
                    if enabstract is None:
                        enabstract = '暂无'
                    fund = doc_tag.front.fund.string
                    if fund is None:
                        fund = '暂无'
                    issue = doc_tag.front.issue.string
                    if issue is None:
                        issue = '暂无'
                    issueNo = doc_tag.front.issueNo.string
                    if issueNo is None:
                        issueNo = '暂无'
                    pageRange = doc_tag.content.find(role="pdfpage").string
                    pages = doc_tag.front.pages.string
                    # print "*" * 30, bookname,id, title, subtitle, englishtitle, englishsubtitle, person_info, key, key_ens, abstract, enabstract, fund, issue, issueNo, pageRange, pages
                    # info = bookname + "_" + id + "_" + title + "\t" + bookname + "_" + id + "\t" + bookname + "\t" + id + "\t" + title + "\t" + subtitle + "\t" + englishtitle + "\t" + englishsubtitle + "\t" + person_info + "\t" + key + "\t" + key_ens + "\t" + abstract + "\t" + enabstract + "\t" + fund + "\t" + issue + "\t" + issueNo + "\t" + pageRange + "\t" + pages + "\n"
                    # write_mapping_log("MagazineTitle.txt", info)
                    # 第三部分获取正文信息：
                    content_file = doc_tag.content.file.string
                    print content_file
                    content = ''
                    for tag in doc_tag.content.find_all(True):
                        if tag.name == 'para':
                            if tag.string is not None:
                                content = content + tag.string
                            else:
                                for string in tag.strings:
                                    content = content + string
                    info = bookname+"_"+id+"_"+title+"\t"+bookname + "\t" + id + "\t" + title + "\t" + del_blank_char(content) + "\n"
                    write_mapping_log("MagazineContent.txt",info)


def get_magazine_titles(srcdir):
    for filename in os.listdir(srcdir):
        file = os.path.join(srcdir, filename)
        if filename.endswith("xml"):
            get_magazine_title(file)


def main():
    srcdir = u"I:\\Deal-Middle\\EXTRACTCDATAXML"
    get_magazine_titles(srcdir)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
