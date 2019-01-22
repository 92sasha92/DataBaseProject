import pymysql

my_cursor = pymysql.cursors.DictCursor


def connect_to_db():
    return pymysql.connect(host="mysqlsrv1.cs.tau.ac.il",
                           user="DbMysql06",
                           passwd="DbMysql06",
                           db="DbMysql06",
                           use_unicode=True, charset="utf8")

