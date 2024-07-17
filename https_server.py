import http.server
import ssl
import os

cert_file = 'localhost.pem'
key_file = 'localhost-key.pem'

server_address = ('localhost', 8000)

os.chdir('frontend')

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

httpd = http.server.HTTPServer(server_address, CustomHTTPRequestHandler)

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=os.path.join('..', cert_file), keyfile=os.path.join('..', key_file))
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Serving on https://localhost:8000")
httpd.serve_forever()
