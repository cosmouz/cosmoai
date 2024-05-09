from wsgiref.simple_server import make_server

def sample_app(environ, start_respone):
    status = "200 OK"
    headers = [("Content-type", "text/plain")]
    start_respone(status, headers)

    return [b"Hello world"]

server = make_server("localhost", 8000, sample_app)
server.serve_forever()