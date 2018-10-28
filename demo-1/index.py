# -*- coding: utf-8 -*-
from flask import Flask, make_response, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return '<p style="color:red;">Hello,World!</p>'


@app.route('/user/<name>')  # 获取URL中的参数
def user(name):
    return 'hello,' + name


@app.route('/test/request')  # 测试request全局变量
def test_request():
    return request.host


@app.route('/test/error')   # 测试抛出错误码
def test_error():
    return '<p>Server error</p>', 400


@app.route('/test/response')    # 测试make_response函数
def test_response():
    res = make_response('123')
    res.set_cookie('user', 'Mari')
    return res


@app.route('/test/redirect')    # 测试重定向
def test_redirect():
    return redirect('http://www.baidu.com')


if __name__ == '__main__':
    app.run(debug=True)


