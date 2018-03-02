'''Echo client program'''
import socket
import sys
import hashlib
import json

class testobj():
    def __init__(self):
        self.string1 = "hello world"
        self.string2 = "this is a string"

def sendobj(sock):
    t1 = testobj()
    serialt1 = json.dumps(t1.__dict__)
    sock.sendall(bytes(serialt1, 'utf-8'))


if len(sys.argv) < 2:
    ipaddr = input("Connect to: ")
    portconn = int(input("Port: "))
else:
    ipaddr = sys.argv[1]
    portconn = int(sys.argv[2])
HOST = ipaddr                 # The remote host
PORT = portconn              # The same port as used by the server
s = socket.socket()
s.connect((HOST, PORT))
print("Connected to:", HOST)
userinput=input("Input data: ")
'''
sendobj(s)
'''
while True:
    s.sendall(bytes(userinput, 'utf-8'))
    data = s.recv(1024)
    userinput = (data.decode())
    print("\tServer echo'd back", userinput)
    print("\tSize of message: %d bytes" %sys.getsizeof(userinput))
    userinput = input("Input data: ")
print("Closing connection.")
