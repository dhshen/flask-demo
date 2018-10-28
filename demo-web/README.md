## DEMO-1

1.创建Python虚拟环境，

```
virtualenv venv
```

2.激活虚拟环境

```
source venv/bin/activate
```

3.安装flask包

```
pip install flask
```

4.编写代码...

```
app.run(debug=True) //开启debug模式可享受代码的热更新能力
```

使用中文时要在文件头部声明编码，

```
# -*- coding: utf-8 -*-
```

否则会报错：

```
SyntaxError: Non-ASCII character '\xe8' in file index.py on line 5, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```



