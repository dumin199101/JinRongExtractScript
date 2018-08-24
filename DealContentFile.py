# coding=utf-8
import re
pattern = re.compile(r'([\u4e00-\u9fa5, ]{1})\s+([\u4e00-\u9fa5, ]{1})')
regex_tab = re.compile("\\t")
# 配置
f2 = open('Content_File.txt','w',encoding="UTF-8")
with open('Check_Content_File.txt','r',encoding='UTF-8') as f:
    i = 1
    while True:
        line = f.readline()
        if len(line) < 1:
            break
        info = regex_tab.split(line)
        string = info[6]
        str2 = pattern.sub(r'\1\2', string)
        # print(info[0],info[1],str2)
        # 原来str2自带换行符
        f2.write(info[0]+"\t"+info[1]+"\t"+info[2]+"\t"+info[3]+"\t"+info[4]+"\t"+info[5]+"\t"+str2)
        print(str(i) + "_"  + info[0] + "_" + info[1]+" Deal Finished...")
        i = i + 1
f2.close()