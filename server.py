
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, world! this is Done by Mahadev')

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = TCPServer(server_address, MyHandler)
    print('Server running on port 8000...')
    httpd.serve_forever()
