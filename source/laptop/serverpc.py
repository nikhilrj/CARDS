from selenium import webdriver
import socket
import time
#import miniRSA
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

countCFGErr = 0
countMemErr = 0

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
	<link href="bootstrap.min.css" rel="stylesheet">

	<!-- Custom styles for this template -->
    <link href="starter-template.css" rel="stylesheet">
  </head>

  <body>

	<div class="container">

	  <div class="starter-template">
		<h1>CARDS</h1>
		<p2 class="lead">Memory Error Detected: {num_memerr}<br></p2>
		<p3 class="lead">Control Flow Error Detected: {num_cfgerr}<br></p3>
		<p4 class="lead">Most Recent Error Detected: {most_recent_err}<br></p4>
		<div style="position: absolute; z-index:100; left: 500px">
            <img id="img1" src="flow_chart.png" width="500" height="600">
         </div>  
         <div style="position: absolute; z-index:5000; left: 500px">
            <img id="img2" src="{cfg_err_src}" width="500" height="600">
         </div>
         <div style="position: absolute; z-index:6000; left: 500px">
            <img id="img3" src="{cfg_err_dst}" width="500" height="600">
         </div>
	  </div>

	</div>

</body></html>
'''

def strToFile(text, filename):
	output = open(filename,"w")
	output.write(text)
	output.close()

def browseLocal(webpageText, filename='ConsoleAppWebpage.html'):
	strToFile(webpageText, filename)
	driver.refresh()

def updateMemErr(message):
	global countMemErr
	countMemErr += 1
	num_memerr = countMemErr
	most_recent_err = "Memeory Corruption Error"

def updateCFGErr(message):
	global countCFGErr
	countCFGErr += 1
	num_cfgerr = countCFGErr
	most_recent_err = "Control Flow Error"

	dest = message.split(' ')[2]
	source = message.split(' ')[-1]

	print("In Update CFG Err Function")

	if dest == "Direction.sensorRead>":
		cfg_err_dst = "fl_sensor_read_red.png"
	elif dest == "ColorSensor.readColor>":
		cfg_err_dst = "fl_read_color_red.png"
	elif dest == "ColorSensor.distance>":
		cfg_err_dst = "fl_distance_red.png"
	elif dest == "PiServer.operation>":
		cfg_err_dst = "fl_server_red.png"
	elif dest == "Direction.calcWeights>":
		cfg_err_dst ="fl_calc_weight_red.png" 
	elif dest == "MotorDriver.drive":
		cfg_err_dst = "fl_drive_red.png"

	if source == "Direction.sensorRead>":
		cfg_err_src = "fl_sensor_read_yellow.png"
	elif source == "ColorSensor.readColor>":
		cfg_err_src = "fl_read_color_yellow.png"
	elif source == "ColorSensor.distance>":
		cfg_err_src = "fl_distance_yellow.png"
	elif source == "PiServer.operation>":
		cfg_err_src = "fl_server_yellow.png"
	elif source == "Direction.calcWeights>":
		cfg_err_src ="fl_calc_weight_yellow.png" 
	elif source == "MotorDriver.drive":
		cfg_err_src = "fl_drive_yellow.png"

def worker():
	num_memerr = "0"
	num_cfgerr = "0"
	most_recent_err = "0"
	cfg_err_src = "empty_img.png"
	cfg_err_dst = "empty_img.png"
	
	while(True):
		raw_msg = sender.recv(size)
		if len(raw_msg) > 0:
			print(raw_msg)
			print("hello")

			if "Memory Corruption Error" in raw_msg:
				global countMemErr
				countMemErr += 1
				num_memerr = countMemErr
				most_recent_err = "Memeory Corruption Error"
			elif "cannot follow" in raw_msg:
				global countCFGErr
				countCFGErr += 1
				num_cfgerr = countCFGErr
				most_recent_err = "Control Flow Error"

				dest = raw_msg.split(' ')[2]
				source = raw_msg.split(' ')[-1]

				print("In Update CFG Err Function")
				print("dest")
				print(dest)
				print("source")
				print(source)

				if dest == "Direction.sensorRead>":
					print("dest is direction")
					cfg_err_dst = "fl_sensor_read_red.png"
				elif dest == "ColorSensor.readColor>":
					print("dest is color sensor")
					cfg_err_dst = "fl_read_color_red.png"
				elif dest == "ColorSensor.distance>":
					print("dest is distance")
					cfg_err_dst = "fl_distance_red.png"
				elif dest == "PiServer.operation>":
					print("dest is server")
					cfg_err_dst = "fl_server_red.png"
				elif dest == "Direction.calcWeights>":
					print("dest is calculate weight")
					cfg_err_dst ="fl_calc_weight_red.png" 
				elif dest == "MotorDriver.drive>":
					print("dest is motor drive")
					cfg_err_dst = "fl_drive_red.png"

				if source == "Direction.sensorRead>'":
					cfg_err_src = "fl_sensor_read_yellow.png"
				elif source == "ColorSensor.readColor>'":
					cfg_err_src = "fl_read_color_yellow.png"
				elif source == "ColorSensor.distance>'":
					cfg_err_src = "fl_distance_yellow.png"
				elif source == "PiServer.operation>'":
					cfg_err_src = "fl_server_yellow.png"
				elif source == "Direction.calcWeights>'":
					cfg_err_src ="fl_calc_weight_yellow.png" 
				elif source == "MotorDriver.drive>'":
					cfg_err_src = "fl_drive_yellow.png"

			print cfg_err_src, cfg_err_dst

			contents = pageTemplate.format(**locals())

			browseLocal(contents)

			print("Refreshed the webpage")

#set thread for receiving message
t = threading.Thread(target=worker) 
t.start()

try:
	while(True):
	
		command = raw_input('Enter a command: ')
		command = command.upper()

		while (command != "RED") and (command != "BLUE"):
			print("Please input either red or blue:")
			command = raw_input('Enter a command: ')
			command = command.upper()

		crypto = rsa.encrypt(command, pubKey)
		print (crypto)
		
		sender.send(crypto)

		# Wait for the interval period
		time.sleep(interval)

		#sender.sendto('ALLOFF', (broadcastIP, broadcastPort))
except KeyboardInterrupt:
	sender.sendto('ALLOFF', (broadcastIP, broadcastPort))
