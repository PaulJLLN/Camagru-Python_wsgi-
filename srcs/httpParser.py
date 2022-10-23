from urllib.parse import unquote

def httpParser(environ):
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 256))
    except (ValueError):
        request_body_size = 0
    response_body = unquote(environ['wsgi.input'].read(request_body_size))
    response_body = response_body.split('&')
    response_body = [tuple(elem.split('=')) for elem in response_body]
    return dict(response_body)