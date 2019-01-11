#encoding:utf-8
from flask import Flask,render_template,url_for
import os
#构造flask对象
app = Flask(__name__)

#网址后面的那根斜杠
@app.route('/')
def hello_world():
    print url_for('hello_world')
    return render_template("h02.html",)  #显示这个网页

@app.route('/h01.html')
def hello_world1():
    s = u"须臾"  # 需要制定编码
    d = [
        {
            "aa": "ha",
            "b": "hb",
            "c": "hc",
        },
        {
            "aa": "ha1",
            "b": "hb",
            "c": "hc",
        }
    ]
    return render_template("h01.html",sdfs=s,book=d)  #显示这个网页

@app.route('/h03.html')
def hello_world2():
    return render_template("h03.html")


@app.route('/h04.html')
def hello_world3():
    f=open(os.path.dirname(__file__)+url_for("static",filename="1.txt"),"r")
    ret=f.read()
    return render_template("h04.html",ha=ret)

if __name__ == '__main__':
    app.run()
# # {%extends"sd.html"%}继承

# 放在父网页
# {%block name%}
# {%endblock%}

#url_for(函数名) #获取此函数的链接地址

#coding:utf-8
# from flask import Flask,render_template,url_for
# import os
#
# app = Flask(__name__)
#
# #url_for将视图函数还原成对应模板页面地址
# @app.route('/')
# def hello_world():#视图函数
#     print os.path.dirname(__file__)
#     f = open(os.path.dirname(__file__)+url_for('static',filename='1.txt'),'r')
#     ret = f.read()
#     return render_template('h04.html',ha = ret)
#
# @app.route('/cot.html')
# def showCot():
#     return render_template('cot.html')
#
#
#
# if __name__ == '__main__':
#     app.run()

