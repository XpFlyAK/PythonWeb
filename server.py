# -*- coding: UTF-8 -*-
import socket
import urllib.parse
from web_demo.web_route import temple_age, temple_home, temple_name, temple_login, temple_register


class Request(object):
    def __init__(self):
        self.path = ''
        self.query = {}
        self.body = ''
        self.method = 'GET'
        self.headers = {}


    def form(self):
        body = urllib.parse.unquote(self.body)
        array = body.split('&')
        f = {}
        for kv in array:
            k, v = kv.split('=')
            f[k] = v
        return f


request = Request()


def log(*args, **kwargs):
    print(args, kwargs)


def parse_path(path):
    if path.find('?') == -1:
        return path, {}
    else:
        request_path = path.split('?')[0]
        query_path = path.split('?')[1]
        f = {}
        query_array = query_path.split('&')
        for x in query_array:
            k, v = x.split('=')
            f[k] = v
        return request_path, f


def parse_path_to_response(path):
    real_path, query = parse_path(path)
    request.query = query
    log(real_path)
    route = {
        '/': temple_home,
        '/name': temple_name,
        '/age': temple_age,
        '/login': temple_login,
        '/register': temple_register,
    }
    response_func = route.get(real_path, error_404)
    return response_func(request)


def error_404(request, error=404):
    e = {
        404: b'HTTP/1.1 404 NOT FOUND\r\n\r\n<h1>NOT FOUND</h1>',
    }
    return e.get(error, b'')


def run(host, port):
    with socket.socket() as s:
        s.bind((host, port))
        while True:
            s.listen(5)
            request_connect, address_address = s.accept()
            rec = request_connect.recv(1000)
            rec = rec.decode('utf-8')
            if len(rec.split()) < 2:
                continue

            print(rec)

            request.body = rec.split('\r\n\r\n')[1]
            request.path = rec.split()[1]
            request.method = rec.split()[0]
            log({'request.body == ': request.body,
                 'request.path == ': request.path})
            parse_response = parse_path_to_response(request.path)
            # header = 'HTTP/1.1 200 Very OK\r\nContent-Type:text/html\r\n'
            # body = '\r\n<h1>Welcome HomePage</h1>'
            request_connect.sendall(parse_response)


if __name__ == '__main__':
    dic = {
        'host': '',
        'port': 2000,
    }
    run(**dic)
