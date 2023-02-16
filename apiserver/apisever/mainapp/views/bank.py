from flask_blueprint import Blueprint
from flask import request, jsonify
from mainapp.dao import bank_dao

blue=Blueprint('bankBlue',__name__)

@blue.route('/bank',methods=['POST','GET'])

def bank():
    dao=bank_dao().BankDao()
    data=dao.find_all()
    # return "<h3>hi,Bank-Blue</h3>"
    return jsonify({
        'status':200,
        'massage':'find_all ok',
        'data':data
    })


@blue.route('/delbank',methods=['POST','GET'])

def del_bank():
    bank_id=request.args.get('bank_id')
    return "<h3>正在删除银行%s</h3>" % bank_id
