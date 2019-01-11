# encoding:utf-8
from flask import Flask,render_template,url_for,request,session,make_response
import MySQLdb,time,random
from datetime import timedelta
import static.P_inner_MCode
from static import P_Image
from io import BytesIO
import base64
from back.lantumain import lantu
app = Flask(__name__)
app.config['SECRET_KEY']="SDFDSFSLSDFJLSJDLFJSDKLJ"
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=3)

app.register_blueprint(lantu,url_prefix='/lantu')  #注册一个蓝图
def ha(str1,str2):
    M=static.P_inner_MCode.m("root","root","t1")
    # 创建数据表SQL语句
    # sql = "CREATE TABLE ss2 ( id  INT(20) NOT NULL,name  CHAR(20),password INT)"
    # 插入数据SQL语句
    # sql1="INSERT ss2 VALU,,ES(1,'one',1234)"
    #查询语句
    sql2="SELECT user,password FROM ss1"

    #获取查询内容 类型为二维元组 元组中的一个小元组代表一行的数据
    t1=M.lian(sql2)

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
    M.close()
def save(arr1):
    M = static.P_inner_MCode.m("root", "root", "t1")
    sql="INSERT ss1(user,password,sex,date) VALUES('%s','%s','%s','%s')"%(arr1[0],arr1[1],arr1[2],arr1[3])

    M.lian(sql)  #在自定义类中获取操作游标，执行sql语句，并返回全部内容

    M.close()  #在自定义类中提交并关闭链接
def yanzheng(arr1):
    M = static.P_inner_MCode.m("root", "root", "t1")
    sql="SELECT user FROM ss1"
    t2=M.lian(sql)
    flag=False
    for i in t2:
        if i[0] == arr1[0]:
            flag = True
    M.close()
    return flag
@app.route('/')
def hello_world2():
    if len(session)>0:#看之前是否登录过
        ct=time.time()-session["time"]
        if ct>30:    #用来判断是否超时
            return render_template("h08_4.html",c=u"登录超时",cc=1)
        return render_template("h08_4.html",c=u"登录成功")
    return render_template("h07_4.html")
@app.route("/1/",methods=["GET","POST"])
def hello_world1():
    h1=request.form.get("user2")
    h2=request.form.get("pw2")
    h3=request.form.get("valid2")
    print h3
    if h3!=None:
        if session['valid1']!=h3:
            return '-1'
    ha(h1, h2)
    if c==u"登录成功":
        session.permanent=True  #启用计时器
        session['us'] = h1
        session['pw'] = h2
        session['time']=time.time()
        return "1"
    else:
        return "0"
@app.route("/2/",methods=["GET","POST"])
def hello_world3():
    h1 = request.form.get("user1")
    h2 = request.form.get("pw1")
    h3 =request.form.get("se")
    h4= request.form.get("da")
    f=yanzheng([h1])
    print(h1,h2,h3,h4)
    if f==False:
        save([h1,h2,h3,h4])
        return '1'
    else:
        return '0'
        # return render_template("h07.html",cc=u"已经存在这个用户")#不能喧染网页了，只能在h07中操作1，0
        # return "000"     #返回的值会自动跟h07.html中的abc关联
@app.route("/1234/")
def hello_world4():
    return render_template("h07_4.html")
@app.route("/1235/",methods=["GET","POST"])
def hello_world5():
    imm,str1=P_Image.getImage()
    buf = BytesIO()  # 构建一个输入输出流
    session['valid1'] = str1
    imm.save(buf,"jpeg")
    buf_str = buf.getvalue()  # 获得输入输出流里面的内容
    response = make_response(buf_str)  # 将返回内容生成一个返回对象
    data1="data:image/"+"jpg;"+"base64,"+base64.b64encode(buf_str)#将图片转为网页中图片标签能识别的字符串
    return data1

if __name__ == '__main__':
    app.run()
# 创建表时 字符用 varchar(10)   用char(20) 不管字符多长都会有20个空间
