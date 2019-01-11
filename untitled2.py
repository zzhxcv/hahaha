# encoding:utf-8
from flask import Flask,render_template
#构造flask对象
app = Flask(__name__)

#网址后面的那根斜杠
@app.route('/')
def hello_world():
    return render_template("h01.html")  #显示这个网页

if __name__ == '__main__':
    app.run()
