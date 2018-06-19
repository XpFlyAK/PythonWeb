# -*- coding: UTF-8 -*-
from web_demo.models.user import User
import json


def temple_name(request):
    head = 'HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n'
    body = '\r\n<h2>The Page is the Name Page</h2>'
    return (head + body).encode('utf-8')


def temple_age(request):
    head = 'HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n'
    body = '\r\n<h2>The Page is the Age Page</h2>'
    return (head + body).encode('utf-8')


def temple_home(request):
    header = 'HTTP/1.1 200 Very OK\r\nContent-Type:text/html\r\n'
    body = '\r\n<h1>Welcome HomePage</h1>'
    return (header + body).encode('utf-8')


def temple_login(request):
    header = 'HTTP/1.1 200 Very OK\r\nContent-Type:text/html\r\n'
    r = render_template_page('login.html')
    if request.method == 'GET':
        r = r.replace('{{message}}', '')
    else:
        f = request.form()
        users = User(f)
        if users.check_user_password():
            r = r.replace('{{message}}', '登陆成功')
        else:
            r = r.replace('{{message}}', '用户名密码错误，登录失败')
    response = header + '\r\n' + r
    return response.encode('utf-8')


def check_dict(f):
    if len(f['user_name']) == 0:
        return False
    else:
        return True


def add_json_file(f):
    with open('json.json', 'r', encoding='utf-8') as r:
        dic = json.load(r)
        print(dic)
        for d in dic:
            if d['user_name'] == f['user_name']:
                print('已经包含了此用户名')
                return
            else:
                print('没有此用户名，可以添加用户')
        dic.append(f)
        print(json.dumps(dic))
        with open('json.json', 'w') as w:
            w.write(json.dumps(dic))


def temple_register(request):
    header = 'HTTP/1.1 200 Very OK\r\nContent-Type:text/html\r\n'
    r = render_template_page('register.html')
    if request.method == 'GET':
        r = r.replace('{{message}}', '')
    else:
        f = request.form()
        if not check_dict(f):
            r = r.replace('{{message}}', '用户名或密码空白')
        else:
            add_json_file(f)
            r = r.replace('{{message}}', '注册成功')
    response = header + '\r\n' + r
    return response.encode('utf-8')


def render_template_page(path):
    file_path = 'templates/' + path
    with open(file_path, 'r', encoding='utf-8') as r:
        return r.read()
