import socket
import time
import miniRSA
import sys

# Settings for the client
broadcastIP = '127.0.0.1'		 # IP address to send to, 255 in one or more positions is a broadcast / wild-card
broadcastPort = 1337					# What message number to send with (LEDB on an LCD)
interval = 0.1						# Time between keyboard updates in seconds, smaller responds faster but uses more processor time
regularUpdate = False					# If True we send a command at a regular interval, if False we only send commands when keys are pressed or released
size = 1024
# Setup the connection for sending on
sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	 # Create the socket

sender.connect((broadcastIP, broadcastPort)) # Set the IP and port number to use locally, IP 0.0.0.0 means all connections and port 0 means assign a number for us (do not care)


def encrypt(privateTuple, data):
        encrypted_data = ""
        for i in range(0, len(data)):
            encrypted_data += str(miniRSA.endecrypt(ord(data[i]), privateTuple[0], privateTuple[1])) + ","
        return encrypted_data


#### MAIN LOOP ###########
e, d, c = miniRSA.keygen()
sendPublic = str(d) + "," + str(c)
sender.send(sendPublic)
print 'Public Key sent to server.'

privateTuple = (e , c)
time.sleep(2)

try:
	while(True):
		# Get the currently pressed keys on the keyboard

    		print 'Enter a command'
		command = raw_input('Enter a command: ')
		data = encrypt(privateTuple, command) 
		print (data)
		
		sender.send(data)

		# Wait for the interval period
		time.sleep(interval)

		#sender.sendto('ALLOFF', (broadcastIP, broadcastPort))
except KeyboardInterrupt:
	sender.sendto('ALLOFF', (broadcastIP, broadcastPort))
	
