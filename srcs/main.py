from wsgiref.simple_server import make_server

from views.View import NotFoundView, SignInView, SignUpView

PORT = 8051
HOST = "0.0.0.0"

ROUTES = {
    "/": SignInView,
    "/signup": SignUpView,
    "404": NotFoundView,
}

def application(environ, start_response):
    for path in ROUTES:
        if (environ["PATH_INFO"] == path):
            instance = ROUTES[path](environ, start_response)
            if (environ["REQUEST_METHOD"] == "GET"):
                return instance.do_GET()
            elif (environ["REQUEST_METHOD"] == "POST"):
                return instance.do_POST()
    return ROUTES['404'](start_response).do_GET()
    

if __name__ == "__main__":
    httpd = make_server(HOST, PORT, application)
    httpd.serve_forever()