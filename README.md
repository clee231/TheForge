# TheForge

General Template

Server

= Genesis: Initialize blockchain with genesis block.
Use Block and Blockchain class from myBlockchain.py.

= Listens for connections (% = infinite thread)

= Listens for received messages:
if message = length flag
send length of own blockchain
if message = block request flag:
find block in own copy of blockchain
send block to that node
if message = new block flag:
authenticate by hashing its blockheader hash and nonce
if Blockheader hash + nonce = Block self hash, then relay block to
all other connections



Client

=Compare length:
ask server for the length of its blockchain
if server length > node's blockchain length
call "get block" index 0, 1, 2, ..., n, until
node length = server length
(In this case it should only be the genesis block)

=if node length = server length
call construct block

=All the block construction code is in myBlockchain.py
once nonce is found, update own blockchain, send it to 
server, restart construction of next block

=Listen for incoming blocks %
if server sends a block, authenticate same way as server does.
Add block to own blockchain, restart construction of next block
with parameters of block you just added

