from wsgiref.simple_server import make_server

from views.signin import SignInView
from views.signup import SignUpView
from views.notfound import NotFoundView

PORT = 8051
HOST = "0.0.0.0"

ROUTES = {
    "/": SignInView,
    "/signup": SignUpView,
    "/notfound": NotFoundView,
}

def application(environ, start_response):
    print(f"PATH_INFO : {environ['PATH_INFO']}")
    for path in ROUTES:
        print(path)
        if (environ["PATH_INFO"] == path):
            if (path != "/notfound"):
                instance = ROUTES[path](environ, start_response)
            else:
                instance = ROUTES[path](start_response)
            if (environ["REQUEST_METHOD"] == "GET"):
                return instance.do_GET()
            elif (environ["REQUEST_METHOD"] == "POST"):
                return instance.do_POST()
    print("Ca part sur du 404")
    return ROUTES['/notfound'](start_response).redirect_to_not_found()
    

if __name__ == "__main__":
    httpd = make_server(HOST, PORT, application)
    httpd.serve_forever()