import socket
import urlparse

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT = 5000

HEALTH_COUNT = 0


class MyHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):

        global HEALTH_COUNT
        parsed_path = urlparse.urlparse(self.path)
        if parsed_path.path == '/health':
            HEALTH_COUNT += 1
            if HEALTH_COUNT <= 5:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                self.wfile.write("healthy " + str(HEALTH_COUNT))
                return
            else:
                self.send_response(500)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                self.wfile.write("unhealthy")
                return
        else:

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Send the html message
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)

            self.wfile.write("Hello World! I'm little cat!\n")
            self.wfile.write("Hostname: " + hostname + "\n")
            self.wfile.write("Ip:       " + ip + "\n")
            return


if __name__ == "__main__":
    server = HTTPServer(('', PORT), MyHandler)
    print 'Started http server on port ', PORT

    # Wait forever for incoming http requests
    server.serve_forever()
