import socket
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT = 5000


class MyHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send the html message
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)

        self.wfile.write("Hello World! I'm little cat!\n")
        self.wfile.write("Hostname: " + hostname + "\n")
        self.wfile.write("Ip:       " + ip + "\n")
        self.wfile.write("Version:  v1\n")
        return


if __name__ == "__main__":
    server = HTTPServer(('', PORT), MyHandler)
    print 'Started http server on port ', PORT

    # Wait forever for incoming http requests
    server.serve_forever()

