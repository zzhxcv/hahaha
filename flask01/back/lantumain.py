#encoding:utf-8
from flask import Blueprint,render_template,url_for,Flask
                               # 指定render_templates ,  指定static_templates
lantu=Blueprint('ha1',__name__,template_folder='hello',static_folder='file1')

# lantu1=Flask(__name__,template_folder="hello")
@lantu.route('/')
def show():
    arr1={'one':{'oo':[1,2,3]},'two':2}
    return render_template('Flask_.html',**arr1)
