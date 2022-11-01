from srcs.httpParser import httpParser

class SignUpView:
    def __init__(self, env, start_fn):
        self._env = env
        self._start_fn = start_fn
    
    def do_GET(self):
        status = '200 OK'
        with open("templates/login.html", "r") as index:
            response_body = index.read()
        response_headers = [
            ('Content-Type', 'text/html'),
            ('Content-Length', str(len(response_body)))
        ]

        self._start_fn(status, response_headers)
        return [response_body.encode()]

    def do_POST(self):
        print("SignUp POST")
        status = '200 OK'

        post_arg = httpParser(self._env)
        response_body = f"{post_arg['login']} vous etes bien connecte."

        response_headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(response_body))),
        ]

        self._start_fn(status, response_headers)
        return [response_body.encode()]