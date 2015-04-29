from selenium import webdriver
#import socketserver
import socket
import webbrowser
import os.path

portListen = 1337
testIP = '127.0.0.1'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((testIP, portListen))
server.listen(5)

size = 1024

conn, client_addr = server.accept()

driver = webdriver.Firefox()
driver.get("file:///" + os.path.abspath('ConsoleAppWebpage.html'))

pageTemplate = '''
<!DOCTYPE html>

<html>
   <head>
      <title>change picture</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
      <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
   </head>

   <body>
      <img id="img1" src="image1.png" class="img-circle" alt="Cinque Terre" width="200" height="200" border="300" style="border:{border1}">
      <img id="img2" src="image2.png" class="img-circle" alt="Cinque Terre" width="200" height="200" border="300" style="border:{border2}">
      <img id="img3" src="image3.png" class="img-circle" alt="Cinque Terre" width="200" height="200" border="300" style="border:{border3}">
      <img id="img4" src="image4.png" class="img-circle" alt="Cinque Terre" width="200" height="200" border="300" style="border:{border4}">
   </body>
</html>
'''

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='ConsoleAppWebpage.html'):
    strToFile(webpageText, filename)
    driver.refresh()

while(True):
    raw_msg = conn.recv(size)
    str_msg = raw_msg.decode('utf-8')
    state_num = int(str_msg)

    border1 = "none"
    border2 = "none"
    border3 = "none"
    border4 = "none"

    if state_num == 1:
        border1 = "5px solid black"
    elif state_num == 2:
        border2 = "5px solid black"
    elif state_num == 3:
        border3 = "5px solid black"
    elif state_num == 4:
        border4 = "5px solid black"

    contents = pageTemplate.format(**locals())

    print(state_num)

    browseLocal(contents)
