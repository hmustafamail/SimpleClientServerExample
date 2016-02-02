#!/bin/env python2.7

# A simple server example
# Mustafa Hussain (TA) For Networks, Dr. Dean Bushey, Spring 2016, FL Poly

# Check Python version
import sys
badVersion = (3,0)
currentVersion = sys.version_info

if currentVersion >= badVersion:
   print("You are using Python 3. Please download Python 2.7 at python.org")
   exit()

import SocketServer

# From https://docs.python.org/2/library/socketserver.html
class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
