# -*- coding: utf-8 -*-
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')  # 返回模板
def index():
    return render_template('index.html')


@app.route('/user')  # 模板赋值
def user():
    return render_template('user.html', name='Jobs')


@app.route('/test/method', methods=['GET', 'POST'])  # 自定义请求方法
def testmethod():
    return 'hello'


@app.errorhandler(404)  # 自定义404页面
def not_found(e):   # 一定要传参，否则会报错
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
