import my_details
#import sshtunnel
import pymysql

my_cursor = pymysql.cursors.DictCursor


'''def tunnel():
    return sshtunnel.SSHTunnelForwarder(
            ('nova.cs.tau.ac.il', 22),
            ssh_username=my_details.username,
            ssh_password=my_details.password,
            remote_bind_address=('mysqlsrv1.cs.tau.ac.il', 3306),
            local_bind_address=('localhost', 3305))

def connect_to_db():
    return pymysql.connect(host="localhost",
                           port=3305,
                           user="DbMysql06",
                           passwd="DbMysql06",
                           db="DbMysql06")'''


def connect_to_db():
    return pymysql.connect(host="mysqlsrv1.cs.tau.ac.il",
                           user="DbMysql06",
                           passwd="DbMysql06",
                           db="DbMysql06",
                           use_unicode=True, charset="utf8")

