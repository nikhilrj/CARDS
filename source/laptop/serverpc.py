import socket
import time

# Settings for the client
broadcastIP = '192.168.0.106'		 # IP address to send to, 255 in one or more positions is a broadcast / wild-card
broadcastPort = 9038					# What message number to send with (LEDB on an LCD)
interval = 0.1						# Time between keyboard updates in seconds, smaller responds faster but uses more processor time
regularUpdate = False					# If True we send a command at a regular interval, if False we only send commands when keys are pressed or released

# Setup the connection for sending on
sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)	 # Create the socket
sender.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)						# Enable broadcasting (sending to many IPs based on wild-cards)
sender.bind(('0.0.0.0', 0))														 # Set the IP and port number to use locally, IP 0.0.0.0 means all connections and port 0 means assign a number for us (do not care)


try:
	while(True):
		# Get the currently pressed keys on the keyboard
		command = raw_input('Enter command to be sent to the Pi')
		sender.sendto(command, (broadcastIP, broadcastPort))

		# Wait for the interval period
		time.sleep(interval)

	sender.sendto('ALLOFF', (broadcastIP, broadcastPort))
except KeyboardInterrupt:
	sender.sendto('ALLOFF', (broadcastIP, broadcastPort))
	