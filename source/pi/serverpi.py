import SocketServer

portListen = 9038

# Class used to handle UDP messages
class InputHandler(SocketServer.BaseRequestHandler):
	# Function called when a new message has been received
	def handle(self):
		global isRunning

		request, socket = self.request		  # Read who spoke to us and what they said
		request = request.upper()			   # Convert command to upper case
		driveCommands = request.split(',')	  # Separate the command into individual drives


if __name__ == '__main__':
	handler = SocketServer.UDPServer(('', portListen), InputHandler)
	while(True)
		handler.handle_request()