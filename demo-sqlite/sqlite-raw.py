# -*- coding: utf-8 -*-
import sqlite3
from flask import *
app = Flask(__name__)
DATABASE_URI = './raw.sqlite'


# @app.before_first_request
def create_db():
    conn = sqlite3.connect(DATABASE_URI)
    c = conn.cursor()
    c.execute('''drop TABLE IF EXISTS user''')
    c.execute('''create table user (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, email TEXT )''')
    users = [('admin', 'admin@ex.com'), ('guest', 'guest@qq.com')]
    c.executemany('INSERT INTO user(name, email) VALUES (?,?)', users)
    conn.commit()
    conn.close()


def get_db():
    db = sqlite3.connect(DATABASE_URI)
    db.row_factory = sqlite3.Row
    return db


@app.route('/user/list')  # 查
def get_list():
    db = get_db()
    sql_req = db.execute('select * from user', ())
    db.commit()
    res = sql_req.fetchall()
    db.close()
    return "<br>".join(["{0}: {1}".format(user[1], user[2]) for user in res])


@app.route('/user/add')  # 增
def add_user():
    db = get_db()
    name = request.args.get('name')
    email = request.args.get('email')
    if name is None:
        abort(500)
    if email is None:
        abort(500)
    db.execute('insert into user(name, email) values(?, ?)', (name, email))
    db.commit()
    db.close()
    return 'add done'


@app.route('/user/del')  # 删
def del_user():
    db = get_db()
    name = request.args.get('name')
    if name is None:
        abort(500)
    db.execute('delete from user where name=?', (name,))  # 传递一个参数时，name后面的[,]非常重要，否则会出错
    db.commit()
    db.close()
    return 'del done'


@app.route('/user/update/<int:id>')  # 改
def update_user(id):
    db = get_db()
    name = request.args.get('name')
    email = request.args.get('email')
    if name is None:
        abort(500)
    if email is None:
        abort(500)
    db.execute('update user set name=?,email=? where id=?', (name, email, id))
    db.commit()
    db.close()
    return 'update done'


if __name__ == '__main__':
    app.run(debug=True)

