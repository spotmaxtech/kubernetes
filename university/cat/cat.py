import socket
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT = 5000

class myHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)

        self.wfile.write("Hello World! I'm little cat!\n")
        self.wfile.write("Hostname: " + hostname + "\n")
        self.wfile.write("Ip:       " + ip)
        return

if __name__ == "__main__":
    try:
        server = HTTPServer(('', PORT), myHandler)
        print 'Started httpserver on port ' , PORT

        # Wait forever for incoming htto requests
        server.serve_forever()

    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()

