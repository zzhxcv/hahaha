# encoding:utf-8
from flask import Flask,render_template
#构造flask对象
app = Flask(__name__)

#网址后面的那根斜杠
@app.route('/')
def hello_world():
    s=u"须臾"        #需要制定编码
    d=[
        {
            "aa":"ha",
            "b":"hb",
            "c":"hc",
        },
        {
            "aa":"ha1",
            "b": "hb",
            "c": "hc",
        }
    ]
    return render_template("h01.html",sdfs=s,book=d)  #显示这个网页
@app.route('/123')
def hello():
    return u'哈哈'    #最好指定编码

@app.route('/456/<abc>')
def hello1(abc):
    return u'哈哈'+abc    #最好指定编码

if __name__ == '__main__':
    app.run()
