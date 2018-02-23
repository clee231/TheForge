# Merkle Experiment

import time
import hashlib

class Tx():
    # Constructor
    def __init__(self, sender, amount, recipient, time):
        self.sender = sender
        self.amount = amount
        self.recipient = recipient
        self.time = time
        self.hash()

    def hash(self):
        hash_key = hashlib.sha256()
        msg = str(self.amount) + str(self.recipient) + str(self.time)
        byte_msg = msg.encode()
        hash_key.update(byte_msg)
        self.cur_hash = hash_key.hexdigest()
#------------------------------------------------------------------------------
def displayTransactions(transactions):
    for i in transactions:
        print("\nTransaction #: %d" % (transactions.index(i)+1))
        print("Name: %s" % i.recipient)
        print("Amount: %s" % i.amount)
        print("The hash for this tx is: \n\t", i.cur_hash)
#------------------------------------------------------------------------------
def rootHash(hash_list):
    index = 0
    callNum = 0
    while ( len(hash_list) > 1):
        callNum += 1
        #print("hashes before function call %d: " %callNum)
        #print("\t", hash_list[index])
        #print("\t", hash_list[index + 1])
        hash_key = hashlib.sha256()
        msg = str(hash_list[index]) + str(hash_list[index+1])
        byte_msg = msg.encode()
        hash_key.update(byte_msg)
        hash_list[index] = hash_key.hexdigest()
        #print("hash after function call %d: " %callNum)
        #print("\t", hash_list[index])
        hash_list.remove(hash_list[index+1])
        if index + 1 == len(hash_list):
            index = 0
        else:
            index += 1
    print("final hash: ")
    print("\t", hash_list)
#------------------------------------------------------------------------------
#Transaction List
transactions = []
#List of hashed transactions
hash_list = []

print("Enter 'x' for recipient when you are done.")

sender = input("What is your account name?")

#Take in transaction data
while True:
    recipient = input("\nWho is the recipient? ")
    if recipient == 'x' and len(transactions) % 2 == 0:
        break
    elif recipient == 'x' and len(transactions) % 2 != 0:
        print("Need an even amount of transactions.\n")
    else:
        amount = input("Amount to send? ")
        txi = Tx( sender, amount, recipient, int(time.time()))
        transactions.append(txi)
        hash_list.append(txi.cur_hash)

#displayTransactions(transactions)

rootHash(hash_list)
