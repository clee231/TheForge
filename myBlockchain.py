
import time
import datetime
import hashlib
import sys
import math

difficultyBaseControl = 5






'''Utility functions'''

def hashThis(myString):
    hashObject = hashlib.sha256()
    hashObject.update(myString.encode())
    return hashObject.hexdigest()

def getTimeStamp(): return float(time.time())

def stopWatch(startTime):
    endTime = int(time.time())
    return endTime - startTime

















'''
Block Class{
        *hash
        *confirmations !
        *size
        *height
        nonce
        *merkleroot !
        *transaction list !
        *time
        *difficulty
        *previous Block Hash
        *print Block Data
}
'''
class Block():


    '''Constructor'''
    def __init__(self, hashPrevBlock, blockchain, transactions):
        self.__hashPrevBlock__ = hashPrevBlock
        self.__height__ = blockchain.getLength()
        self.__transactions__ = transactions
        self.__setMerkleRoot__()
        self.__setTarget__()




    '''Setters'''
    def __setMerkleRoot__(self):
        m = str(self.__transactions__)
        self.__merkleroot__ = hashThis(m)

    def __setBlockHeader__(self):
        m = str(self.__timestamp__) + str(self.__height__) + str(self.__merkleroot__) + str(self.__hashPrevBlock__) + str(self.__nonce__)
        self.__blockHeader__ = hashThis(m)

    '''Every x blocks, the difficulty increases by one zero'''
    def __setTarget__(self):
        self.__difficulty__ = difficultyBaseControl + int(self.__height__/100)
        self.__target__ = ''.join(['0' for x in range(self.__difficulty__)])

    def __setMineTime__(self):
        self.__mineTime__ = int(time.time())








    '''Meat and Potatoes'''
    def findNonce(self):
        self.__nonce__ = 0
        self.__timestamp__ = getTimeStamp()
        self.__setBlockHeader__()
        while not self.__blockHeader__[0:self.__difficulty__] == self.__target__:
            self.__nonce__ += 1
            self.__setBlockHeader__()
            if self.__nonce__ % 250007 == 0:
                print('.', end = ' ', flush = True)
        print("\n")
        self.__setMineTime__()
        self.__size__ = sys.getsizeof(self)






    '''Getters'''
    def getBlockHash(self): return self.__blockHeader__

    def getNonce(self): return self.__nonce__

    def getHeight(self): return self.__height__

    def getSize(self): return self.__size__

    def getTransactionList(self): return self.__transactions__

    def getBlockTimestamp(self): return self.__timestamp__

    def getMerkleRoot(self): return self.__merkleroot__

    def getPrevHash(self): return self.__hashPrevBlock__

    def getDifficulty(self): return self.__difficulty__

    def getMineTime(self):
        return datetime.datetime.fromtimestamp(self.__mineTime__).strftime('%Y-%m-%d %H:%M:%S')
























'''
Class Blockchain{
    *Genesis protocol
    *Genesis block
    *Adds blocks
    *Block reward !
    *Executes payout to miner wallet !
    *Halving Block Reward !
}
'''
class Blockchain():



    '''Constructor'''
    def __init__(self):
        self.__length__ = 0
        self.__createGenesis__()
        self.__supply__ = 0
        self.__blockList__ = []
        self.addBlock(self.__genesisBlock__)

    '''After tx list in Block class this will have to be changed'''
    def __createGenesis__(self):
        genesisPrevHash = "00000000000000000000000000000000"
        data = "SIG Blockchain"
        genesisBlock = Block(genesisPrevHash, self, data)
        genesisBlock.findNonce()
        self.__genesisBlock__ = genesisBlock






    '''Meat and Potatoes'''
    def addBlock(self, newBlock):
        self.__blockList__.append(newBlock)
        self.__latestBlock__ = newBlock
        self.__length__ += 1
        self.__generateCoin__()

    def __generateCoin__(self):
        power = int(self.__length__ / 20)
        amount = float(50 / 2**power)
        self.__supply__ += amount




    '''Getters'''
    def getLatestBlock(self): return self.__latestBlock__

    def getLength(self): return self.__length__

    def getGenesisBlock(self): return self.__genesisBlock__

    def getSupply(self): return self.__supply__


    '''FIXME'''
    def getBlockbyHash(self, searchHash):
        for x in self.__blockList__:
            if x.getBlockHash() == searchHash:
                return x
        print ("Block could not be found.")

    '''FIXME'''
    def getBlockbyIndex(self, index):
        currentBlock = self.getLatestBlock()
        iterations = currentBlock.getHeight() - index
        if iterations < 0:
            print("Block has not been mined yet.")
        elif index >= self.getLength() / 2:
            for x in range(iterations):
                prevHash = currentBlock.getPrevHash()
                currentBlock = self.getBlockbyHash(prevHash)
        else:
            currentBlock = self.getGenesisBlock()
            for x in range(iterations- 1):
                nextHash = currentBlock.getNextHash()
                currentBlock = getBlockbyHash(nextHash)
        return currentBlock











''' SANDBOX '''


print("Initializing...\n")
myBlockchain = Blockchain()

print("Genesis achieved.")
print("Genesis block hash is \n\t%s" % myBlockchain.getLatestBlock().getBlockHash())
print("Length of blockchain is: %d block." % myBlockchain.getLength())
print("Current difficulty is set to: %d prefixed zeros." % myBlockchain.getGenesisBlock().getDifficulty())
print("Let us begin...\n")





while True:
    #myData = input("Data: ")
    myData = 100
    newBlock = Block(myBlockchain.getLatestBlock().getBlockHash(), myBlockchain, myData)
    newBlock.findNonce()
    myBlockchain.addBlock(newBlock)

    print("Newest block hash is: \n\t%s" % newBlock.getBlockHash())
    print("Nonce: %d" % newBlock.getNonce())
    print("Block was mined %s" % newBlock.getMineTime())
    print("Length of blockchain is: %d blocks." % myBlockchain.getLength())
    print("Current difficulty is set to: %d prefixed zeros." % newBlock.getDifficulty())
    print("Supply: %f.\n" % myBlockchain.getSupply())
    myData += 1
