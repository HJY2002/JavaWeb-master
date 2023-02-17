from flask_blueprint import Blueprint
from flask import request,render_template

#创建蓝图的时候第一个参数name可以随便写，第二个参数必须使用__name__，表示导包的名称
blue=Blueprint('userBlue',__name__)

#声明API接口
@blue.route('/user/user',methods=['GET','POST'])
def user():
    return "<h2>hi,User - Blueprint</h2>"

#声明API接口
@blue.route('/find',methods=['GET'])
def find():
    print('url',request.url)
    print('base_url',request.base_url)
    print('host_url',request.host_url)
    print('path',request.path)
    return render_template('user_list.html',request=request)
