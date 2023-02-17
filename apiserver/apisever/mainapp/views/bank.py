from flask_blueprint import Blueprint
from flask import request, jsonify, make_response, Response
from mainapp.dao import bank_dao

blue = Blueprint('bankBlue', __name__)


@blue.route('/bank', methods=['POST', 'GET'])
def bank():
    dao = bank_dao().BankDao()
    data = dao.find_all()
    # return "<h3>hi,Bank-Blue</h3>"
    return jsonify({
        'status': 200,
        'massage': 'find_all ok',
        'data': data
    })


@blue.route('/edit/<int:bank_id>', methods=['POST', 'GET'])
def edit(bank_id):
    return "<h3>正在编辑银行编号%s</h3>" % bank_id


@blue.route('/forward/<path:url>', methods=['GET', 'POST'])
def forward(url):
    return """
        <script>
            let steps=5;
            let id=setInterval(()=>{
            if(steps>=1){
                document.write("剩余"+(--steps)+"秒");}
            else{
                open("%s",target="_self")%url;
            }        
                    },1000)
        </script>
    """


@blue.route('/find/<keyworld>/', methods=['POST', 'GET'])
def edit(keyward):
    # keyworld的类型可以是int 或者string
    return "<h3>keyword的类型为：%s，值是%s</h3>" % (type(keyward), keyward)


@blue.route('/publish', methods=['POST'])
def publish_bank():
    data = '{"id":101,"age":"20"}'
    code = 200
    #将数据和相应的状态代码封装到response对象中
    # response = make_response(data, code)
    #根据数据的类型，设置响应头
    # response.headers['Content-Type'] = 'application/json;charset=utf-8'
    # return response
    # return  jsonify({data,code})
    response = Response(data=data, status=code, mimetype='application/json;charset=utf-8')
    return response


@blue.route('/delbank', methods=['POST', 'GET'])
def del_bank():
    bank_id = request.args.get('bank_id')
    return "<h3>正在删除银行%s</h3>" % bank_id
