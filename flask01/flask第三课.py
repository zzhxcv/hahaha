# encoding:utf-8
from flask import Flask,render_template,url_for,session
import os
from datetime import timedelta
app=Flask(__name__)
app.config["SECRET_KEY"]=os.urandom(24)  #session存在cokien里面    这句代码加密信息

                                             #时间戳
app.config["PERMANENT_SESSION_LIFETIME"]=timedelta(days=7)  #cookie保存时间
@app.route('/')
def show1():
    session["pass"]="1234"
    session["ha"]="23432432421342"
    session.permanent=True   #要打开权限才能设置保存时间

    return"hello world"
@app.route("/1")
def show2():
    return session['pass']+"     "+session["ha"]

@app.route("/12")
def show3():
    session.clear()#删除所有
    # session.pop("pass")#删除单个
    return "ok"
if __name__=="__main__" :
    app.run()

