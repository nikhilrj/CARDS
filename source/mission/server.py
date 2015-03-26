import sys
import os
import socket
import SocketServer
import rsa
import time

class PiServer():

	def __init__(self, Ip = '127.0.0.1', port = 1337, sz = 2048, keySz = 1024):
		self.testIP = Ip
		self.portListen = port
		self.size = sz
		self.bitKeySize = keySz

		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((testIP, portListen))
		server.listen(1)

		conn, client_addr = server.accept()

		print 'Connected to Client.'

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

	#### Loop to receive messages
	def serverOperation(self):

		encryptedMessage = conn.recv(size)
		decryptedMessage = rsa.decrypt(encryptedMessage, privKey)
	   	print decryptedMessage.upper()
