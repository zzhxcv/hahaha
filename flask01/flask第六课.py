# encoding:utf-8
from flask import Flask,request,render_template
import MySQLdb

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

#把用户注册信息存入数据库
def save(arr1):
    db = MySQLdb.connect("localhost", "root", "root", "t1", charset='utf8')

    # # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql="INSERT ss2(name,password) VALUES('%s','%s')"%(arr1[0],arr1[1])
    cursor.execute(sql)
    db.commit()
    db.close()

#用户注册时的验证
def yanzheng(arr1):
    db = MySQLdb.connect("localhost", "root", "root", "t1", charset='utf8')

    # # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    sql="SELECT name FROM ss2"

    cursor.execute(sql)

    t2=cursor.fetchall()
    flag=False
    for i in t2:
        if i[0] == arr1[0]:
            flag = True
    db.commit()
    db.close()
    return flag


import peizhi.peizhi01

app = Flask(__name__)
app.config.from_object(peizhi.peizhi01) #引用外部配置文件
@app.route('/')
def hello_world():
    return render_template("h06.html")

@app.route('/1',methods=["GET","POST"])
def hello_world1():
    if request.method=="GET":
       ha( request.form.get("user"),request.form.get("pw"))   #查询数据库看登录是否成功
    else:
       arr1=[request.form.get("user"), request.form.get("pw")]

       ha(request.form.get("user"),request.form.get("pw"))#查询数据库中是否有这个用户名和密码

       f=yanzheng(arr1)   #判断数据库中是否存在 此 用户名

       if f==False:
           save(arr1) #把注册的账号密码存入数据库
           return render_template("h06.html",ccc=u"存储成功")
       else:

           return render_template("h06.html",cc=u"已经存在该用户")
    # return render_template("h06.html",c=c)

if __name__ == '__main__':
    app.run()
