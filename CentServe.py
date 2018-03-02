import myBlockchain
import test_suite
import threading
import socket
import json
import sys


class Cent():
    def __init__(self):
        self.blockchain = Blockchain()
        self.HOST = ''
        self.PORT = 10000
        self.connections = []
        self.s = socket.socket()
        self.s.bind((HOST,PORT))
        self.s.listen(1)
        print("Listening for connections...")
        run()

    '''Run threads'''
    def run(self):
        listenThread = threading.Thread(target = self.recv_msg())
        listenThread.daemon = True
        listenThread.start()
        while True:
            conn, addr = s.accept()
            self.connections.append(conn)

    def recv_msg(self):
        data = self.s.recv(1024)

    def genesis(self):

    def send_blockchain(self):

    def auth_incoming_block(self):

    def relay_block(self):
