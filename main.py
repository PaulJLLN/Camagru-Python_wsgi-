from wsgiref.simple_server import make_server

from srcs.views.signin import SignInView
from srcs.views.signup import SignUpView
from srcs.views.notfound import NotFoundView
from srcs.views.gallery import GalleryView
from srcs.views.edit import EditView
from srcs.views.index import IndexView

PORT = 8051
HOST = "0.0.0.0"
IP = "10.11.4.5"

ROUTES = {
    "/": IndexView,
    "/signin": SignInView,
    "/signup": SignUpView,
    "/edit": EditView,
    "/gallery": GalleryView,
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