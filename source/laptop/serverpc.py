from selenium import webdriver
import socket
import time
import sys
import rsa
import threading
import webbrowser
import os.path

# Settings for the client
broadcastIP = '192.168.0.102'		 # IP address to send to, 255 in one or more positions is a broadcast / wild-card
broadcastPort = 9038					# What message number to send with (LEDB on an LCD)
interval = 0.1						# Time between keyboard updates in seconds, smaller responds faster but uses more processor time
regularUpdate = False					# If True we send a command at a regular interval, if False we only send commands when keys are pressed or released
size = 2048
# Setup the connection for sending on
sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	 # Create the socket

sender.connect((broadcastIP, broadcastPort)) # Set the IP and port number to use locally, IP 0.0.0.0 means all connections and port 0 means assign a number for us (do not care)
print ('connected')
### Process of Receiving Public Key ###
pubKeyN = sender.recv(size)
print (pubKeyN)
pubKeyN = long(pubKeyN)
time.sleep(1)
pubKeyE = sender.recv(size)
print (pubKeyE)
pubKeyE = long(pubKeyE)


pubKey = rsa.PublicKey(pubKeyN,pubKeyE)

print ('Public Key received from server.')

driver = webdriver.Firefox()
driver.get("file:///" + os.path.abspath('ConsoleAppWebpage.html'))

pageTemplate = '''
<!DOCTYPE html>
<!-- saved from url=(0051)http://getbootstrap.com/examples/starter-template/# -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<title>CARDS</title>

	<!-- Bootstrap core CSS -->
	<link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">

	<!-- Custom styles for this template -->
	<link href="http://getbootstrap.com/examples/starter-template/starter-template.css" rel="stylesheet">

  </head>

  <body>

	<div class="container">

	  <div class="starter-template">
		<h1>CARDS</h1>
		<p1 class="lead">Fault Injected: {num_injected}<br></p1>
		<p2 class="lead">Memory Error Detected: {num_memerr}<br></p2>
		<p3 class="lead">Control Flow Error Detected: {num_cfgerr}<br></p3>
		<img id="img1" src="flow_chart.png" width="800" height="800">
	  </div>

	</div>

</body></html>
'''

def strToFile(text, filename):
	youtput = open(filename,"w")
	output.write(text)
	output.close()

def browseLocal(webpageText, filename='ConsoleAppWebpage.html'):
	strToFile(webpageText, filename)
	driver.refresh()

def worker():
	while(True):
		raw_msg = sender.recv(size)
		str_msg = raw_msg.decode('utf-8')
		num_injected = "0"
		num_memerr = "0"
		num_cfgerr = "0"

		num_injected = str_msg
		contents = pageTemplate.format(**locals())

		browseLocal(contents)
		
	
	
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
