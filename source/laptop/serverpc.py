import socket
import time
import miniRSA
import sys
import rsa
import threading

# Settings for the client
broadcastIP = '192.168.0.102'		 # IP address to send to, 255 in one or more positions is a broadcast / wild-card
broadcastPort = 9038					# What message number to send with (LEDB on an LCD)
interval = 0.1						# Time between keyboard updates in seconds, smaller responds faster but uses more processor time
regularUpdate = False					# If True we send a command at a regular interval, if False we only send commands when keys are pressed or released
size = 2048
# Setup the connection for sending on
sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	 # Create the socket

sender.connect((broadcastIP, broadcastPort)) # Set the IP and port number to use locally, IP 0.0.0.0 means all connections and port 0 means assign a number for us (do not care)
print 'connected'
### Process of Receiving Public Key ###
pubKeyN = sender.recv(size)
print pubKeyN
pubKeyN = long(pubKeyN)
time.sleep(1)
pubKeyE = sender.recv(size)
print pubKeyE
pubKeyE = long(pubKeyE)


pubKey = rsa.PublicKey(pubKeyN,pubKeyE)

print 'Public Key received from server.'



def worker():
	while(True):
		print(sender.recv(size))
	
	
	
time.sleep(2)

#set thread for receiving message
t = threading.Thread(target=worker) 
t.start()

try:
	while(True):
	
		command = raw_input('Enter a command: ')
		crypto = rsa.encrypt(command, pubKey)
		print (crypto)
		
		sender.send(crypto)

		# Wait for the interval period
		time.sleep(interval)

		#sender.sendto('ALLOFF', (broadcastIP, broadcastPort))
except KeyboardInterrupt:
	sender.sendto('ALLOFF', (broadcastIP, broadcastPort))
	
	
