import RPi.GPIO as GPIO
import sys,tty,termios,time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Setup GPIO
GPIO.setup (5, GPIO.OUT)    
GPIO.setup (7, GPIO.OUT)      
GPIO.setup (10, GPIO.OUT)    
GPIO.setup (12, GPIO.OUT)

#Enable Signals
GPIO.setup (3, GPIO.OUT)
GPIO.output(3,True)
GPIO.setup (8, GPIO.OUT)
GPIO.output(8,True)


#GPIO.setup (3, GPIO.OUT)#LED
#GPIO.output(3,True)
#ledstate = True

#def getch():
#    fd=sys.stdin.fileno()
#    old_settings=termios.tcgetattr(fd)
#    try:
#        tty.setraw(sys.stdin.fileno())
#        ch=sys.stdin.read(1)
#    finally:
#        termios.tcsetattr(fd,termios.TSCADRAIN,old_settings)
#    return cd
#
while 1:
    control=raw_input()

    if (control == "a"):
        GPIO.output(5,True)
    
    if (control == "d"):
        GPIO.output(7,True)

    if (control == "w"):
        GPIO.output(12,True)
    
    if (control == "s"):
        GPIO.output(10,True)

    if (control == "q"):    
 #       GPIO.output(3,False)#LED
        sys.exit("Bye!")
     
    time.sleep(.5)
    GPIO.output(10,False)
    GPIO.output(12,False)
    GPIO.output(5,False)
    GPIO.output(7,False)
  #  ledstate=not ledstate
  #  GPIO.output(3,ledstate)

    
