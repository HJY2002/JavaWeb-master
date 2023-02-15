from flask import Flask
from flask import render_template
from flask import request

# 创建Flask对象 -Httpd WEB服务对象
app = Flask(__name__)  # _name_可以是任意小写字母，表示Flask应用对象名称


# 声明WEB服务的请求资源（指定资源访问的路由）
@app.route('/bank', methods=['GET', 'POST', 'CONNECT', 'DELETE', 'PUT', 'PATCH'])
def bank():
    # 加载数据(Model交互操作)
    data = {
        'title': '银行',
        'error': '加载错误'
    }
    # 渲染模板
    """html = render_template('bank.html', **data)
    print(html+'\n')
    raise Exception('测试异常')
    return html"""

    if request.method == 'GET':
        return render_template('bank.html', **data)
    else:
        #处理POST请求
        #获取表单参数
        name=request.form.get('name',None)
        card_num=request.form.get('card_num',None)
        if all((name,card_num)):
            app.logger.info('name:%s->card:%s'%(name,card_num))#日志输出
            return """<h2>信息正确</h2>
                    <h4 id="result"></h4>
                    <script>
                        let steps=5;
                        let interval_id=0;
                        setInterval(()=>{
                            if(steps>=0){
                                document.getElementById("result").innerHTML=steps--;
                            }else{
                            //取消定时器
                            clearInterval(interval_id);
                            window.open('/hi',target='_self');
                            
                        },1000)
                    </script>"""
        else:
            data['error'] = '参数错误'
            return render_template('bank.html', **data)


# 启动flask的服务器
app.run('localhost', 5000,
        True,#默认未开启调试模式，TRUE为开启调试模式
        threaded=True,#默认为FALSE，单线程
       # processes=10#默认只有1个进程，多进程跟多线程无法同时开启
        )
