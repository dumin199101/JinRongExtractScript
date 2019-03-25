#coding=utf-8
import sys
import urllib
import urllib2
import re
import json
import jsonpath
import uuid

re_digit = re.compile(r"\d+")
regex_tab = re.compile(r"\t")


def del_blank_char(str):
    rep = re.compile(r'(\n|\t|\r)')
    (fstr, count) = rep.subn('', str)
    return fstr


def write_mapping_log(logname, content):
    with open(logname, "a+") as f1:
        f1.write(content.encode("utf-8"))


def get_law_info(name,link):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "BIDUPSID=2E06FE8CC4CB97DE206096AFD27FF47C; PSTM=1514785883; MCITY=-142%3A; BAIDUID=0412E235172CD30A794401B979EF2903:FG=1; BDUSS=lEQTRESGVjV29FSlZMWlJvRFF6VE5CNH5kMEJnckJwTTA4ZnF4M3BkU0JSN2RjQVFBQUFBJCQAAAAAAAAAAAEAAABFt0sfc2hhbmc0NDMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIG6j1yBuo9cSn; BDSFRCVID=92DsJeCCxG3t7879u4sJDqRS65rxbHHuLBs73J; H_BDCLCKID_SF=tJkJVI-aJK83j-OghKTfjjQybmT22-us-bFJ2hcH0KLKM4jhBnAheJQ3XRJ3txtjfIQl3CQOWfb1MRjvef8MjPPJ0J6R0-oWWgI8Ll5TtUJqJKnTDMRh-xCwbfcyKMnitIj9-pnKfpQrh459XP68bTkA5bjZKxtq3mkjbIOFfD_2MDD9D58Ken-W5gTW-4o05I60WnI8Kb7V-P5mhqn5hnLX-U__5t3J5-ctLn67KbjVqbjYbPIX-joQ-HLh-R3LXKj-0nTaaC6HhDtrej5UKUI8LPbO05JJJb-fV4K2-hcUqfobj6oK2-Dnyhor3Jtft2LE3-oJqC8KhKtR3J; H_PS_PSSID=1463_21112_28723_28557_28697_28584_26350_28604_28627_28606; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=1; __guid=232297866.1813158410672979000.1553417069064.252; monitor_count=12; Hm_lvt_ac8fb11c31cd3cf585523fd58e170e95=1553417070,1553417145,1553417188,1553417365; Hm_lpvt_ac8fb11c31cd3cf585523fd58e170e95=1553417365",
        "Host": "duxiaofa.baidu.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    request = urllib2.Request(link, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    json_html = json.loads(html)

    # 获取目录
    chapter_list = jsonpath.jsonpath(json_html, "$.data.mainBody[0].content[*].title")
    for chapter in chapter_list:
        if chapter is None:
            break
        print name,chapter
        # write_mapping_log("Law_Chapter_GUID.txt",str(uuid.uuid1()).upper().replace("-","")+"\t"+name+"\t"+chapter+"\n")

    # 获取条目及其正文
    # item_list = jsonpath.jsonpath(json_html, "$.data.mainBody[0].content[*].content[*]")
    # for item in item_list:
    #     title = item.get('title')
    #     index = item.get('index')
    #     text = del_blank_char(item.get('text'))
    #     print name,index, title, text
    #     write_mapping_log("Law_Items.txt",name+"\t"+str(index)+"\t"+title+"\t"+text+"\n")

    # 获取章节跟正文
    # doc_text = ''
    # chapter_list = jsonpath.jsonpath(json_html, "$.data.mainBody[0].content[*]")
    # for chapter in chapter_list:
    #     chapter_title = chapter.get('title')
    #     # if chapter_title is None:
    #     #     break
    #     chapter_content = chapter.get('content')
    #     chapter_text = ''
    #     for item in chapter_content:
    #         title = item.get('title')
    #         # print title
    #         text = item.get('text')
    #         chapter_text = chapter_text + del_blank_char(text)
    #     # print name,chapter_title,chapter_text
    #     # write_mapping_log("Law_Chapter.txt",name+"\t"+chapter_title+"\t"+chapter_text+"\n")
    #     # 全文正文
    #     doc_text = doc_text + chapter_text
    # print name,doc_text
    # write_mapping_log("Law_Book.txt",name+"\t"+doc_text+"\n")





def get_laws(srcfile):
    with open(srcfile, "r") as f1:
        i = 1
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            law_name = info[0]
            law_link = info[1]
            print i,law_name
            get_law_info(law_name,law_link)
            i = i + 1


def main():
    # link = u"https://duxiaofa.baidu.com/law/Ajax/detail?type=statute&cid=5f21fd1e3684b3f4cba1d24720c4adbd_law"
    # get_law_info(link)
    srcfile = "Law.txt"
    get_laws(srcfile)



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()
