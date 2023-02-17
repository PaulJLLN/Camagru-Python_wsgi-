class EditView:
    def __init__(self, env, start_fn):
        self._start_fn = start_fn
    
    def do_GET(self):
        status = '200 OK'
        with open("templates/edit.html", "r") as index:
            response_body = index.read()
        response_headers = [
            ('Content-Type', 'text/html'),
            ('Content-Length', str(len(response_body))),
        ]

        self._start_fn(status, response_headers)
        return [response_body.encode()]

    def do_POST(self):
        pass
    