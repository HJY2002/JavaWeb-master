from flask_blueprint import Blueprint
from flask import url_for
blue = Blueprint('cardBlue', __name__)
@blue.route('/add<bankName>/<int:page>')
def add(bankName,page):
    return "%s开户成功!在第%s页"%(bankName,page)
@blue.route('/select_bank')
def select_bank():
    #查询所有银行，供用户选择
    #用户选择后，进入开户行首页
    bankName="中国银行"
    return """
        选择成功,3秒后<a href=“%s”></a>进入开户行
    """ % url_for('cardBlue.add', bankName=bankName,page=1)#h函数的第一个参数为蓝图名.函数名，第二个参数为url
        #url_for("函数名", **kwargs) 反向解析获取flask的路由注册的路径
        #url_for('蓝图名.函数名'**kwargs) 反向解析指定蓝图下的路由注册的路径