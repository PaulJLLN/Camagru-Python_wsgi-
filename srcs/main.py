from wsgiref.simple_server import make_server
from json import dumps

from httpParser import httpParser
PORT = 8051
HOST = "0.0.0.0"

def do_get_signup(environ, start_response):
    status = '200 OK'
    with open("templates/signup.html", "r") as index:
        response_body = index.read()
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body.encode()]

def do_post_signup(environ, start_response):
    status = '200 OK'
    
    post_arg = httpParser(environ)
    response_body = f"{post_arg['login']} vous etes bien enregistre !"

    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body.encode()]


def application (environ, start_response):
    if environ["REQUEST_METHOD"] == "GET":
        return do_get_signup(environ, start_response)
    elif environ["REQUEST_METHOD"] == "POST":
        return do_post_signup(environ, start_response)

if __name__ == "__main__":
    httpd = make_server(HOST, PORT, application)
    
    print(f"The server is listening on the following address: {HOST}:{PORT}")
    httpd.serve_forever()