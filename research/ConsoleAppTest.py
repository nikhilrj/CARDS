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

def parseErrorType(str_msg)
    
    return err_type

while(True):
    raw_msg = conn.recv(size)
    str_msg = raw_msg.decode('utf-8')
    parsed = parseString(str_msg)
    num_injected = "0"
    num_memerr = "0"
    num_cfgerr = "0"

    contents = pageTemplate.format(**locals())

    print(state_num)

    browseLocal(contents)