import sys
import os
import socket
import SocketServer
import threading
import miniRSA
import rsa
import time

testIP = '127.0.0.1'
portListen = 1337
size = 2048
bitKeySize = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((testIP, portListen))
server.listen(1)

conn, client_addr = server.accept()

print 'Connected to Client.'

### Process of generating a public and private key ###
(pubKey, privKey) = rsa.newkeys(bitKeySize)

pubKeyN = pubKey.n
pubKeyE = pubKey.e
pubKeyN = str(pubKeyN)
pubKeyE = str(pubKeyE)
print pubKeyN
print pubKeyE
conn.send(pubKeyN)
time.sleep(1)
conn.send(pubKeyE)

print 'Client Public key sent.'

#### Loop to receive messages
def serverOperation():

	encryptedMessage = conn.recv(size)
	print (encryptedMessage)
	decryptedMessage = rsa.decrypt(encryptedMessage, privKey)
   	print decryptedMessage.upper()
