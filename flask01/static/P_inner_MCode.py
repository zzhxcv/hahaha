#encoding:utf-8
import MySQLdb
class m(object):
    def __init__(self,user,password,ku):
        self.db=MySQLdb.connect('127.0.0.1',user,password,ku,charset='utf8')

    def lian(self,sql):
        cursor=self.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def close(self):
        self.db.commit()
        self.db.close()
