# encoding:utf-8
import MySQLdb
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template,url_for

# app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql1+mysqldb://root:root@127.0.0.1:3306/Flask_?charset=utf8"
# db = SQLAlchemy(app)
# db.create_all()
#
# @app.route("/")
# def show():
#     return "hello haha"
#
# if __name__=="__main__":
#     app.run()


db = MySQLdb.connect("localhost", "root", "root", "t1", charset='utf8' )

# # 使用cursor()方法获取操作游标
cursor = db.cursor()

# # 使用execute方法执行SQL语句
# 如果数据表已经存在使用 execute() 方法删除表。
# cursor.execute("DROP TABLE IF EXISTS EMPL")

# 创建数据表SQL语句
# sql = """CREATE TABLE ss1 (
#          id  CHAR(20) NOT NULL,
#          name  CHAR(20),
#          age INT,
#          sex CHAR(1)
#           )"""

# 插入数据SQL语句
sql1="insert ss1 values(1,1,1,1)"

try:
   # 执行sql语句
   cursor.execute(sql1)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()