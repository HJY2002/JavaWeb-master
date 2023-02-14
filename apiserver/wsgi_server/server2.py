from flask import Flask

# 创建Flask对象 -Httpd WEB服务对象
app = Flask(__name__)  # _name_可以是任意小写字母，表示Flask应用对象名称


# 声明WEB服务的请求资源（指定资源访问的路由）
@app.route('/hello', methods=['GET', 'POST', 'CONNECT', 'DELETE', 'PUT', 'PATCH'])
def hello():
    from flask import request
    # request是请求对象（HttpRequest），它包含请求资源的路径、请求方法、请求头、上传的表单数据、文件等信息
    # 获取请求中查询参数
    name = request.args.get('username')
    password = request.args.get('password')

    return """
        <h1>用户登录信息</h1>
        <h3>用户名：%s</h3>
        <h3>口令：%s</h3>
    """%(name, password)

def hi():
    from flask import request
    #检测访问请求的方式
    if request.method=='GET':
        #检测访问平台
        platform = request.args.get('platform')
        if platform.lower() !='android':
            return """当前仅支持Android平台"""

#启动flask的服务器
app.run(host='0.0.0.0', port=5000)