import hashlib
from txgen import Tx
import time
from nonce_gen import nonce_get, verify_nonce

# Merkle tree generator
class Merkle_tree:

    def __init__(self, transactions):
        self.hashlist(transactions)
        self.make_tree()

    # Takes list of transactions and hashes each item
    # This now forms a list of hashes
    def hashlist(self, transactions):
        self.hashlist = []
        for i in transactions:
            sha = hashlib.sha256()
            m = str(i.sender) + str(i.amount) + str(i.recipient) + str(i.time)
            sha.update(m.encode())
            this_hash = sha.hexdigest()
            self.hashlist.append(this_hash)

    # Algorithm for finding merkle root
    def make_tree(self):

        # Declaration of lists
        hashlist = self.hashlist
        temp_list = []

        # For every pair of hashes in the list we iterate
        for index in range(0, len(hashlist), 2):
            # Marks the currently selected hash
            current = hashlist[index]

            # Designates what is being paired withe the current hash
            if index + 1 != len(hashlist):
                after_current = hashlist[index + 1]
            else:
                after_current = ''

            # Combines hashes
            sha = hashlib.sha256()

            if after_current != '':
                m = current + after_current
                sha.update(m.encode())
            else:
                sha.update(current.encode())

            comb_hash = sha.hexdigest()

            temp_list.append(comb_hash)

        # Checks to see if list has been reduced to one item
        if len(temp_list) != 1:
            self.hashlist = temp_list
            self.make_tree()
        else:
            self.tree_hash = temp_list[0]

    def get_treehash(self):
        return self.tree_hash

# TEST-------------------------------------------------------------------------
transactions = []

for i in range(0,3):
    contract = Tx(i+2, i+1, i)
    transactions.append(contract)

testmerkle = Merkle_tree(transactions)
rootHash = testmerkle.get_treehash()
print(rootHash)

this_nonce = nonce_get(rootHash)

verify_nonce(rootHash, this_nonce)
# TEST-------------------------------------------------------------------------
