# -*- coding: utf-8 -*-
from flask import *
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello,index.'


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['testfile']
    f.save('./files/' + secure_filename(f.filename))
    return 'ok'
# 测试命令：curl -F "testfile=@test.png" http://127.0.0.1:5000/upload


if __name__ == '__main__':
    app.run(debug=True)

