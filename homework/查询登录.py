# encoding:utf-8
import MySQLdb
from flask import Flask,render_template,request

def ha(str1,str2):
    db = MySQLdb.connect("localhost", "root", "root", "t1", charset='utf8' )

    # # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # # 使用execute方法执行SQL语句
    # 创建数据表SQL语句
    sql = "CREATE TABLE ss2 ( id  INT(20) NOT NULL,name  CHAR(20),password INT)"
    # 插入数据SQL语句
    sql1="INSERT ss2 VALUES(1,'one',1234)"
    #查询语句
    sql2="SELECT name,password FROM ss2"

    try:
       # 执行sql语句
       # cursor.execute(sql)#创表

       # cursor.execute(sql1)#插入

       #查询账号和密码
       cursor.execute(sql2)

       #获取查询内容 类型为二维元组 元组中的一个小元组代表一行的数据
       t1=cursor.fetchall()

       #定义标志位 判断是否在数据库中
       flag=False
       for i in t1:
           if i[0]==str1 and i[1]==int(str2):
               flag=True
       if flag:
           global c
           c=u"登录成功"
       else:                               #（（1，1），（2，2），（3，3））
           c=u"登录失败"
       # 提交到数据库执行
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    # 关闭数据库连接
    db.close()

app=Flask(__name__)

@app.route("/")
def show():
    return "hello"

# http://127.0.0.1:5000/login/?user=one&pw=1234
@app.route('/login/',methods=['GET','POST'])
def show1():
    if request.method == 'GET':
        ha(request.args.get('user'),request.args.get('pw'))
    else:
        print 'post'
    return render_template('h01.html',c=c)
if __name__=="__main__":
    app.run()

#get 提交数据方式   直接写在网址的后面
#post提交数据方式   没有写后面也收到了

