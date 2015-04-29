import sys 
import os 
import socket 
import SocketServer 
import rsa 
import time, select
  
from control import *
#from variable import *
#global mission

class PiServer():

	#def __init__(self, Ip = '127.0.0.1', port = 1337, sz = 2048, keySz = 256):

	### Process of generating a public and private key ###

	def keyExchange(self):

		(pubKey, self.privKey) = rsa.newkeys(bitKeySize)
		pubKeyN = pubKey.n
		pubKeyE = pubKey.e
		pubKeyN = str(pubKeyN)
		pubKeyE = str(pubKeyE)
		conn.send(pubKeyN)
		time.sleep(1)
		conn.send(pubKeyE)

		print 'Client Public key sent.'

	def operation(self, motors=None):
		global CFC
		CFC.update(PiServer.operation)

		if select.select([conn], [], [], 0)[0]:
			encryptedMessage = conn.recv(size)
			decryptedMessage = rsa.decrypt(encryptedMessage, self.privKey)
			print decryptedMessage.lower()
			
			motors.drive(25, 25)
			#time.sleep(1)
			return decryptedMessage.lower()

	def send(self, msg):
		conn.send(str(msg))


	def __eq__(self, other):
		return self.__dict__ == other.__dict__

	def __repr__(self):
		return self.__dict__.__str__()		

if __name__ == '__main__':
	server = PiServer()
	server.keyExchange()
	while True:
		print server.serverOperation()


testIP = '192.168.0.102'
portListen = 9038
size = 2048
bitKeySize = 256
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((testIP, portListen))
server.listen(1)

conn, client_addr = server.accept()

print 'Connected to Client.'
