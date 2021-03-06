from __future__ import print_function
import u6
import time
import os
import pigpio
import sys

d = u6.U6()
d.getCalibrationData()

MIN_WIDTH=775
MAX_WIDTH=2175

SERVO_PIN=3

width = 875

pi = pigpio.pi()

if not pi.connected:
   exit()

def convert(inByte2, inByte3):
    combined = inByte2*256 + inByte3
    return combined




for q in xrange(int(sys.argv[1])):
    cmdList=[]



    state16 = (q%4)//2
    if state16 >= 1:
        s16 = 1
    else:
        s16 = 0

    s15 = (q%2)

    if time.clock() < .5:
        pi.set_servo_pulsewidth(SERVO_PIN, MIN_WIDTH)
    elif time.clock() > .5 and time.clock() < 1:
        pi.set_servo_pulsewidth(SERVO_PIN, width)
    else:
        pi.set_servo_pulsewidth(SERVO_PIN, MIN_WIDTH)
        

    d.setDOState(16,s15)
    d.setDOState(17,s16)

    d.setDOState(4,0)

    results = d.spi([0x00, 0])
    inByte1 = results['SPIBytes'][0]
    inByte2 = results['SPIBytes'][1]
    results = d.spi([0x00, 0])
    inByte3 = results['SPIBytes'][0]


    print(s15, s16, end=':')

    print (convert(inByte2, inByte3))
    


    d.setDOState(4,1)

    time.sleep(.01)














#cmdList.append(on15)
###cmdList.append(on16)
#cmdList.append(off17)
#d.getFeedback(cmdList)

# cmdList.append(on20)
# cmdList.append(off21)
# cmdList.append(off22)
# d.getFeedback(cmdList)

# cmdList.append(off20)
# cmdList.append(off21)
# cmdList.append(on22)
# d.getFeedback(cmdList)

#d.setDOState(16,1)
#d.setDOState(17,0)