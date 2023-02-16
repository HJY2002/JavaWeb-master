from flask_blueprint import Blueprint
from flask import request

#创建蓝图的时候第一个参数name可以随便写，第二个参数必须使用__name__，表示导包的名称
blue=Blueprint('userBlue',__name__)

#声明API接口
@blue.route('/user/user',methods=['GET','POST'])
def user():
    return "<h2>hi,User - Blueprint</h2>"

#声明API接口
@blue.route('/find',methods=['GET'])
def find():
    return "<h2>hi,User - Blueprint</h2>"
