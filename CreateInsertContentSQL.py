# coding=utf-8
import re
import pymysql


# mysqlHelper
def connDB():
    # 连接数据库
    conn = pymysql.connect(host="", port=3306,user="root", passwd="", db="test", charset='utf8mb4');
    cur = conn.cursor()
    return (conn, cur)


def exeUpdate(conn, cur, sql):
    # 更新或插入操作
    sta = cur.execute(sql)
    conn.commit()
    return (sta)


def exeQuery(cur, sql):
    # 查找操作
    cur.execute(sql)
    return (cur)


def connClose(conn, cur):
    # 关闭连接，释放资源
    cur.close()
    conn.close()


def write_mapping_log(logname, content):
    """
    生成mapping日志文件
    :return:
    """
    with open(logname, "a+",encoding="utf-8") as f1:
        f1.write(content)


def create_insert_content_sql(txtfile):
    """
    直接生成插入SQL脚本存在转译问题
    :param txtfile:
    :return:
    """
    regex_tab = re.compile("\\t")
    (conn, cur) = connDB()
    with open(txtfile,encoding="utf-8") as f1:
        i = 1
        while True:
            line = f1.readline()
            if len(line) < 1:
                break
            info = regex_tab.split(line)
            sql = 'INSERT INTO `tb_content`(`bookname`,`title`,`tree`,`pdfpage`,`bookpage`,`relationkey`,`content`) VALUES (\"%s\",\"%s\",\"%s\",%d,%d,\"%s\",%s);'
            content = conn.escape(info[6])
            sql = sql % (
            info[0], info[1], info[2], int(info[3]), int(info[4]), info[5],content)

            (sta) = exeUpdate(conn, cur, sql)

            if sta < 0:
               write_mapping_log("debug_insertconentsql.log",info[0] + "_" + info[1]+"\n")
            else:
                print(str(i)+"_"+info[0] + "_" + info[1])
                i = i + 1






def main():
    # 配置数据
    content_txt_file = "Content_File.txt"
    create_insert_content_sql(content_txt_file)


if __name__ == '__main__':
    main()
