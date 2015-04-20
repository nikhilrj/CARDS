import sys 
import os 
import socket 
import SocketServer 
import rsa 
import time, select
  
from control import *

class PiServer():

	#def __init__(self, Ip = '127.0.0.1', port = 1337, sz = 2048, keySz = 256):

	### Process of generating a public and private key ###

	def keyExchange(self):

		(pubKey, privKey) = rsa.newkeys(bitKeySize)
		pubKeyN = pubKey.n
		pubKeyE = pubKey.e
		pubKeyN = str(pubKeyN)
		pubKeyE = str(pubKeyE)
		conn.send(pubKeyN)
		time.sleep(1)
		conn.send(pubKeyE)

		print 'Client Public key sent.'

	def operation(self):
		global CFC
		CFC.update(PiServer.operation)

		if select.select([conn], [], [], 0)[0]:
			encryptedMessage = conn.recv(size)
			decryptedMessage = rsa.decrypt(encryptedMessage, privKey)
	   		return decryptedMessage.lower()


	def __eq__(self, other):
		return self.__dict__ == other.__dict__
		

if __name__ == '__main__':
	server = PiServer()
	server.keyExchange()
	while True:
		print server.serverOperation()


testIP = '127.0.0.1'
portListen = 1337
size = 2048
bitKeySize = 256
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((testIP, portListen))
server.listen(1)

conn, client_addr = server.accept()

print 'Connected to Client.'
