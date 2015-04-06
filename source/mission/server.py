import sys
import os
import socket
import SocketServer
import rsa
import time, select

from control import *

class PiServer():

	def __init__(self, Ip = '127.0.0.1', port = 1337, sz = 2048, keySz = 256):
		self.testIP = Ip
		self.portListen = port
		self.size = sz
		self.bitKeySize = keySz

		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((self.testIP, self.portListen))
		server.listen(1)

		self.conn, self.client_addr = server.accept()

		print 'Connected to Client.'

	### Process of generating a public and private key ###

	def keyExchange(self):

		(pubKey, self.privKey) = rsa.newkeys(self.bitKeySize)
		pubKeyN = pubKey.n
		pubKeyE = pubKey.e
		pubKeyN = str(pubKeyN)
		pubKeyE = str(pubKeyE)
		self.conn.send(pubKeyN)
		time.sleep(1)
		self.conn.send(pubKeyE)

		print 'Client Public key sent.'

	def operation(self):
		global CFC
		CFC.update(PiServer.operation)

		if select.select([self.conn], [], [], 0)[0]:
			encryptedMessage = self.conn.recv(self.size)
			decryptedMessage = rsa.decrypt(encryptedMessage, self.privKey)
	   		return decryptedMessage.lower()


if __name__ == '__main__':
	server = PiServer()
	server.keyExchange()
	while True:
		print server.serverOperation()
