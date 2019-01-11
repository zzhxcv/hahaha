# encoding:utf-8

from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def show():
    return "hello"

# @app.route("/login/",methods=["GET","POST"])
# def show1():
#     return render_template("h05.html")


# http://127.0.0.1:5000/login/?user=xiaoming&pw=123456
@app.route('/login/',methods=['GET','POST'])
def show1():
    if request.method == 'GET':
        print request.args.get('user')
        print request.args.get('pw')
    else:
        print 'post'
    return render_template('h05.html')


if __name__=="__main__":
    app.run()
#get 提交数据方式   直接写在网址的后面
#post提交数据方式   没有写后面也收到了

