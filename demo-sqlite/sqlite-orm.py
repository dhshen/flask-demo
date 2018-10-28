# -*- coding: utf-8 -*-
import os
from flask import *
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name


# @app.before_first_request
def create_db():
    db.drop_all()
    db.create_all()
    admin = User('admin', '124124124@qq.com')
    db.session.add(admin)
    guestes = [User('guest1', 'guest1@example.com'),
               User('guest2', 'guest2@example.com'),
               User('guest3', 'guest3@example.com'),
               User('guest4', 'guest4@example.com')]
    db.session.add_all(guestes)
    db.session.commit()


@app.route('/user/')  # 查询所有
def index():
    users = User.query.all()
    return "<br>".join(["{0}: {1}".format(user.name, user.email) for user in users])


@app.route('/user/<int:id>')  # 根据用户ID查询用户
def user(id):
  user = User.query.filter_by(id=id).one()
  return "{0}: {1}".format(user.name, user.email)


@app.route('/user/add')  # 根据GET请求参数新增用户
def add_user():
    name = request.args.get('name')
    email = request.args.get('email')
    if name is None:
        abort(400)
    if email is None:
        abort(400)
    test = User(name, email)
    db.session.add(test)
    db.session.commit()
    return str(test.id)  # 返回插入数据的ID


@app.route('/user/del/<string:name>')   # 根据名字删除行
def del_user(name):
    user = User.query.filter_by(name=name).one()
    db.session.delete(user)
    db.session.commit()
    return 'done'


@app.route('/user/update/<int:id>')     # 修改
def update_user(id):
    name = request.args.get('name')
    email = request.args.get('email')
    if name is None:
        abort(400)
    if email is None:
        abort(400)
    user = User.query.filter_by(id=id).first()
    user.name = name
    user.email = email
    db.session.commit()
    return 'done'


if __name__ == '__main__':
    app.run(debug=True)

