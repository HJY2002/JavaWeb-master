from unittest import TestCase
import requests


#声明单元测试类
class TestBank(TestCase):
    #声明单元测试的方法
    #方法以“test_”开头
    def test_del(self):
        url = 'http://127.0.0.1:5000/bank/del/100'
        method = 'DELETE'
        resp = requests.request(method, url)

        #断言 最后一个参数表示断言失败的信息
        self.assertIs(resp.status_code, 200,'请求失败')
        print(resp.text)
    def test_publish(self):
        url="http://localhost:5000/bank/publish"
        method = 'post'
        resp = requests.post(url)
        self.assertEqual(resp.status_code, 200,'请求失败')
        print(resp.text)
