import myBlockchain
import test_suite
import threading
import socket
import sys

class Node():
    '''Constructor'''
    def __init__(self):
        len(sys.argv) = argc
        if argc < 2:
            self.HOST = input("IP: ")
            self.PORT = input("Port: ")
        else:
            self.HOST = sys.argv[1]
            self.PORT = sys.argv[2]
        self.connect_me()
        self.run()

    '''Connect to server'''
    def connect_me(self):
        self.s = socket.socket()
        self.s.connect((self.HOST, self.PORT))
        print("Connected to:" self.HOST)

    '''Run threads'''
    def run(self):
        sendThread = threading.Thread(target = self.send_msg())
        sendThread.daemon = True
        sendThread.start()
        while True:
            self.recv_msg()





    '''Outgoing'''
    def send_msg(self):
        while True:
            self.s.send(bytes(input("")), 'utf-8')

    '''Incoming'''
    def recv_msg(self):
        data = self.s.recv(1024)

    '''def download_blockchain(self):'''

    '''def construct_next_block(self):'''

    '''def auth_incoming_block(self):'''

    '''def broadcast_block(self):'''
