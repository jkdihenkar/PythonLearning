#!/usr/bin/python3.6
import socketserver
import os
import sys

unix_domain_socket_addr = "./py3.sock"

# socketserver.ThreadingTCPServer()
class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper() + "\n".encode("utf-8"))

def eat_what_you_kill(ADDRESS):
    print("Fatal/Graceful Shutdown. Removing {}".format(ADDRESS))
    os.remove(ADDRESS)

if __name__ == "__main__":
    ADDRESS = "./py3.sock"
    sys.excepthook = lambda x, y, z: eat_what_you_kill(ADDRESS)

    # Create the server, binding to localhost on port 9999
    with socketserver.UnixStreamServer(ADDRESS, MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

# Test client by running - echo "hello" | nc -U ./py3.sock