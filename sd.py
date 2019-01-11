# encoding:utf-8
import MySQLdb
def ha():
    db = MySQLdb.connect("localhost", "root", "root", "t1", charset='utf8' )

    # # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # # 使用execute方法执行SQL语句
    # 创建数据表SQL语句
    sql = "CREATE TABLE ss2 ( id  INT(20) NOT NULL,name  CHAR(20),password INT)"
    # 插入数据SQL语句
    sql1="INSERT ss2 VALUES(1,'one',1234)"
    #查询语句
    sql2="SELECT name,password FROM ss2 Where name='one'"

    try:
       # 执行sql语句
       # cursor.execute(sql)#创表

       # cursor.execute(sql1)#插入

       #查询账号和密码
       print cursor.execute(sql2)

       #获取查询内容 类型为二维元组 元组中的一个小元组代表一行的数据
       # t1=cursor.fetchall()

       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    # 关闭数据库连接
    db.close()



