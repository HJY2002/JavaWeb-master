from mainapp import app
from flask_script import Manager
from mainapp.views import bank,user
from flask_cors import CORS
if __name__ == '__main__':
    CORS.init_app(app)
    #将蓝图对象注册到flask服务中
    app.register_blueprint(bank.blue)
    app.register_blueprint(user.blue ,url_prefix='/user')#url_prefix是前缀，表示url的前缀
    #以脚本的方式启动flask应用服务
    manager = Manager(app)
    manager.run()