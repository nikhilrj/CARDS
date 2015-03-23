import socket
import time

#from enum import Enum

broadcastIP = '127.0.0.1'
broadcastPort = 1337
interval = 1
regularUpdate = False

sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sender.connect((broadcastIP, broadcastPort))

STATE_INP  = 1
STATE_OUT  = 2
STATE_EVEN = 3
STATE_ODD  = 4

SIG_INP  = 1
SIG_ODD  = 2
SIG_EVEN = 3
SIG_OUT  = 4

class StateMachine:
    pass

inp = StateMachine()
inp.stateName   = STATE_INP
inp.signature   = SIG_INP
inp.difference  = SIG_INP ^ SIG_OUT
inp.nextState   = inp

odd = StateMachine()
odd.stateName   = STATE_ODD
odd.signature   = SIG_ODD
odd.difference  = SIG_ODD ^ SIG_INP
odd.nextState   = odd

even = StateMachine()
even.stateName  = STATE_EVEN
even.signature  = SIG_EVEN
even.difference = SIG_EVEN ^ SIG_INP
even.nextState  = even

out = StateMachine()
out.stateName   = STATE_OUT
out.signature   = SIG_OUT
out.difference  = SIG_OUT ^ SIG_EVEN
out.nextState   = out

out_var = ''
inp_var = 0
G = SIG_INP

def driveState(state):

    global inp_var
    global out_var
    global G

    if state.stateName == STATE_INP:
        inp_var = int(input())
        if (inp_var % 2) == 0:
            state.nextState = even
            G = G ^ state.nextState.difference
        else:
            state.nextState = odd
            G = G ^ state.nextState.difference
        
    elif state.stateName == STATE_OUT:
        print(out_var)
        state.nextState = inp
        G = G ^ state.nextState.difference

    elif state.stateName == STATE_EVEN:
        out_var = "EVEN"
        state.nextState = out
        G = (G ^ state.nextState.difference) ^ (0)

    elif state.stateName == STATE_ODD:
        out_var = "ODD"
        state.nextState = out
        G = (G ^ state.nextState.difference) ^ (even.signature ^ odd.signature)

    assert G == state.nextState.signature


state = inp

try:
    while(True):
        driveState(state)
        state = state.nextState
        sender.sendto((bytes(str(state.stateName))), (broadcastIP, broadcastPort))

        # Wait for the interval period
        time.sleep(interval)

    sender.sendto('ALLOFF', (broadcastIP, broadcastPort))

except KeyboardInterrupt:
    sender.sendto('ALLOFF', (broadcastIP, broadcastPort))

