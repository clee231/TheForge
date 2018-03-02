'''Echo server program'''
import socket
import threading
import sys
import json

def recobj(data):
    try:
        deserialt1 = json.loads(data.decode())
    except json.decoder.JSONDecodeError:
        pass
    print("Deserialized: ", deserialt1['string1'])


def handler(conn, addr):
    while True:
        try:
            data = conn.recv(1024)
            print("Data received from client: ", data.decode())
            for conn in connections:
                conn.sendall(data)
            if not data:
                connections.remove(conn)
                conn.close()
                print("Client disconnected.")
                break
        except:
            pass
        '''
        recobj(data)
        '''


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 10000              # Arbitrary non-privileged port
s = socket.socket()
connections = []
s.bind((HOST, PORT))
s.listen(10)
print("Listening for clients...")
while True:
    conn, addr = s.accept()
    recThread = threading.Thread(target=handler, args=(conn,addr))
    recThread.daemon = True
    recThread.start()
    connections.append(conn)
    print('Connected by', addr)
