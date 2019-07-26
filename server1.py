# A simple server example
# Mustafa Hussain, MS

import sys
import socketserver

# From https://docs.python.org/2/library/socketserver.html
class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        '''
        This method is called when the server receives a message
        '''

        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()

        # Print something to the console
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        
        # Capitalize the message and send it back
        self.request.sendall(self.data.upper())

if __name__ == "__main__":

    # This server is going to run on port 9999, on this computer
    HOST = "localhost"
    PORT = 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
