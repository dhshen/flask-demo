# Nginx + uWSGI + Flask

参考链接：[在 Ubuntu 上使用 uWSGI 和 Nginx 部署 Flask 项目](https://lufficc.com/blog/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu)

1.在服务器上安装virtualenv

```
pip install virtualenv
```

2.在项目目录下创建虚拟环境

```
virtualenv venv
```

3.激活虚拟环境

```
source venv/bin/active
```

4.安装flask包

```
pip install flask
```

5.编写代码...



## Nginx配置

```
server{
    listen 80;
    server_name xxx.xxx.com;
    
    location /{
        include uwsgi_params;
        uwsgi_pass unix:/path/to/sock/example.sock;
    }
}
```

当Nginx访问出现502等错误时，可以打开Nginx错误日志排查错误原因。一开始遇到sock文件目录写错与权限不够的问题时都通过日志排查解决了。



