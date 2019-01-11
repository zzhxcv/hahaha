# encoding:utf-8
from flask import Flask,render_template,url_for,request,session
import MySQLdb,time
from datetime import timedelta
app = Flask(__name__)
app.config['SECRET_KEY']="SDFDSFSLSDFJLSJDLFJSDKLJ"
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=3)

def ha(str1,str2):
    db = MySQLdb.connect("localhost", "root", "root", "t1", charset='utf8' )
    # # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # # 使用execute方法执行SQL语句
    # 创建数据表SQL语句
    # sql = "CREATE TABLE ss2 ( id  INT(20) NOT NULL,name  CHAR(20),password INT)"
    # 插入数据SQL语句
    # sql1="INSERT ss2 VALU,,ES(1,'one',1234)"
    #查询语句
    sql2="SELECT user,password FROM ss1"
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
           if i[0]==str1 and i[1]==str2:
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

def save(arr1):
    db = MySQLdb.connect("localhost", "root", "root", "t1", charset='utf8')

    # # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql="INSERT ss1(name,password,sex) VALUES('%s','%s','%s')"%(arr1[0],arr1[1],arr1[2],arr[3])
    cursor.execute(sql)
    db.commit()
    db.close()

def yanzheng(arr1):
    db = MySQLdb.connect("localhost", "root", "root", "t1", charset='utf8')
    # # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    sql="SELECT user FROM ss1"

    cursor.execute(sql)

    t2=cursor.fetchall()
    flag=False
    for i in t2:
        if i[0] == arr1[0]:
            flag = True
    db.commit()
    db.close()
    return flag
@app.route('/')
def hello_world2():
    if len(session)>0:
        ct=time.time()-session["time"]
        if ct>30:
            return render_template("h08.html",c=u"登录超时",cc=1)
        return render_template("h08.html",c=u"登录成功")
    return render_template("h07.html")
@app.route("/1/",methods=["GET","POST"])
def hello_world1():
    h1=request.form.get("user")
    h2=request.form.get("pw")

    print(h1,h2)
    ha(h1,h2)
    if c==u"登录成功":
        session.permanent=True  #启用计时器
        session['us'] = h1
        session['pw'] = h2
        session['time']=time.time()

    return render_template("h08.html",c=c)
@app.route("/2/",methods=["GET","POST"])
def hello_world3():
    h1 = request.form.get("user1")
    h2 = request.form.get("pw1")
    h3 =request.form.get("se")
    h4= request.form.get("da")
    f=yanzheng([h1])
    print(h1,h2,h3,h4)
    if f==False:
        # save([h1,h2,h3])
        # return render_template("h07.html",cc=u"注册成功 请登录")
        return "100"
    else:
        # return render_template("h07.html",cc=u"已经存在这个用户")
        return "000"     #返回的值会自动跟h07.html中的abc关联

@app.route("/1234/")
def hello_world4():
    return render_template("h07.html")

if __name__ == '__main__':
    app.run()
# 创建表时 字符用 varchar(10)   用char(20) 不管字符多长都会有20个空间

































