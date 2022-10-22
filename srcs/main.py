from wsgiref.simple_server import make_server

PORT = 8051
HOST = "0.0.0.0"

def application (environ, start_response):
    print("It hits !")
    response_body = "Hello World!"
    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body.encode()]


if __name__ == "__main__":
    httpd = make_server(HOST, PORT, application)
    
    print(f"The server is listening on the following address: {HOST}:{PORT}")
    httpd.serve_forever()