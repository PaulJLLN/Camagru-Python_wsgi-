class NotFoundView:
    def __init__(self, start_fn):
        self._start_fn = start_fn
    
    def do_GET(self):
        status = '404 Not Found'
        with open("templates/notFound.html", "r") as index:
            response_body = index.read()
        response_headers = [
            ('Content-Type', 'text/html'),
            ('Content-Length', str(len(response_body))),
        ]

        self._start_fn(status, response_headers)
        return [response_body.encode()]

    def redirect_to_not_found(self):
        print("redirect to not found")
        status = "302 See Other"
        with open("templates/notFound.html", "r") as index:
            response_body = index.read()
        response_headers = [
            ('Content-Type', 'text/html'),
            ('Content-Length', str(len(response_body))),
            ('Location', "http://10.11.4.7:8051/notfound")
        ]
        self._start_fn(status, response_headers)
        return [response_body.encode()]
    