# A simple client example
# Mustafa Hussain, MS

import sys
import socket

# We will write to the server at their address.
HOST = "localhost"

# We also need to know their "apartment number" to get our message to them.
PORT = 9999

# This gets all the stuff on the command line after the name of the program.
userWords = sys.argv[1:]

# The stuff comes in as a list. Let's join it all together to get a big string.
data = " ".join(userWords)

# Create a socket (SOCK_STREAM for a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This means "Do this, knowing it might fail..."
try:
    # Connect to server.
    sock.connect((HOST, PORT))
    
    # Send our message to the server. 
    # '\n' is known as the newline character.
    # It's what happens when you hit the ENTER key in a text editor.
    message = data + "\n"
    sock.sendall(message.encode('utf-8'))

    # Receive the message from the server.
    received = sock.recv(1024).decode('utf-8')
    
# "...and whether or not it fails, close the socket safely."
finally:
    sock.close()

# This shows the user what we sent to the sever...
print("Sent:     {}".format(data))

# ...and what we got back from the server.
print("Received: {}".format(received))

