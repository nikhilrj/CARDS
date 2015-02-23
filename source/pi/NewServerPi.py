import sys
import os
import socket
import SocketServer
import threading
import miniRSA

testIP = '127.0.0.1'
portListen = 1337
size = 1024


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((testIP, portListen))
server.listen(5)

conn, client_addr = server.accept()

key = conn.recv(size)
key = key.split(',')
keyTuple = (key[0], key[1])

print 'Client Public key Received'

## decrypt function ##
def decrypt(keyTuple, buff):
        """
        Decrypts input integer list into sentences
        """

        words = buff.split(",")
        decrypted_data = ""
        # print words;
        # sys.exit();
        for i in range(0, len(words) - 1):
            decrypted_data += str(miniRSA.decode(miniRSA.endecrypt(words[i], keyTuple[0], keyTuple[1])))
        return decrypted_data

#### Loop to receive messages 
while(True):

	encryptedMessage = conn.recv(size)
	print (encryptedMessage)
   	decryptedMessage = decrypt(keyTuple, encryptedMessage)
   	print decryptedMessage.upper()
