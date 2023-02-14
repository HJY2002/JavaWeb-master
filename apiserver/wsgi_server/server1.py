from wsgiref.simple_server import make_server


def app(env, make_response):
    # 处理业务的最核心的函数
    for k, v in env.items():
        print(k,':',v)
    #生成响应的头
    make_response('200 ok', [('Content-Type','text/html;charset=utf-8')])
    return ['<h1>Hello World</h1>'.encode('utf-8')]#响应数据


host = '0.0.0.0'
port = 8000
httpd = make_server(host, port, app)
print('服务器启动成功 http://%s:%s' % (host, port))
#启动服务，开始监听客户端链接
httpd.serve_forever()
