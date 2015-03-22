#!/usr/bin/env python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from time import time

PORT = 8080
FLAG = "insert-flag-here"

# type, brew time
teas = {'/ceylon': 240,
        '/chai': 240,
        '/chamomile': 120,
        '/darjeeling': 180,
        '/earl-grey': 240,
        '/english-breakfast': 300,
        '/flag': 60,
        '/green': 60,
        '/jasmine': 60,
        '/lavender': 300}

brewing = {}

class BrewHandler(BaseHTTPRequestHandler):
    error_message_format = '''
        <head>
        <title>Error %(code)d</title>
        </head>
        </body>
        <h1>Error %(code)d</h1>
        <p>%(message)s
        '''
    server_version = "Teapot/1.0"
    sys_version = ""

    def __init__(self, request, client_address, server):
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def do_GET(self):
        self.send_error(418, "I am a teapot.")

    def do_PROPFIND(self):
        self.send_error(418, "I am a teapot.")

    def do_WHEN(self):
        self.send_error(418, "I am a teapot.")

    def do_POST(self):
        self.brew(False)

    def do_BREW(self):
        self.brew(True)

    def brew(self, brew):
        global time
        ctype = self.headers.gettype()
        address = self.client_address[0]
        message = self.rfile.read(int(self.headers["Content-Length"]))

        if message == "stop":
            if address in brewing:
                endtime, tea, br, sugar = brewing[address]
                dt = time() - endtime
                if not brew or not br:
                    self.send_error(400, "This tea tastes a bit deprecated.")
                elif tea == "/flag" and not sugar:
                    self.send_error(400, "I like my flag tea with a bit of sugar.")
                elif dt < teas[tea]-5:
                    self.send_error(400, "This tea tastes a bit too weak.")
                elif dt > teas[tea]+5:
                    self.send_error(400, "This tea tastes a bit too strong.")
                else:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write("Ahh! That was a marvelous cup of tea!")
                    if tea == "/flag":
                        self.wfile.write("<br>Oh, I found this flag at the bottom of the cup: " + FLAG)
                del brewing[address]
            else:
                self.send_error(400, "Not brewing!")
            return

        if ctype in ["message/teapot", "message/coffeepot"] and self.path == "/":
            self.send_response(300)
            alternates = ",".join(['{"%s" {type message/teapot}}'%tea for tea in sorted(teas)])
            self.send_header("Alternates", alternates)
            self.end_headers()
        elif ctype != "message/teapot":
            self.send_error(415, "Unsupported message type.")
        elif message != "start":
            self.send_error(400, "Invalid message.")
        elif self.path not in teas:
            self.send_error(404, "Tea not found.")
        elif address in brewing:
            self.send_error(400, "Already brewing!")
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write("Brewing...")
            sugar = "Accept-Additions" in self.headers and "sugar" in self.headers["Accept-Additions"].lower()
            brewing[address] = (time(), self.path, brew, sugar)

def main():
    try:
        server = HTTPServer(('', PORT), BrewHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()

if __name__ == '__main__':
    main()
