"""
The default SPI settings for a U6 are:

  AutoCS = True, DisableDirConfig = False, SPIMode = 'A', SPIClockFactor = 0,
  CSPinNum = 0 (FIO0), CLKPinNum = 1 (FIO1), MISOPinNum = 2 (FIO2),
  MOSIPinNum = 3 (FIO3)

Note the CSPinNum, CLKPinNum, MISOPinNum, and MOSIPinNum pin numbers and make
your connections accordingly.
"""
from __future__ import print_function
import os
import time

import u6
d = u6.U6() #Open first found U6 over USB

def convert(inByte2, inByte3):
    combined = inByte2*256 + inByte3
    return combined

while(True):
    d.setDOState(4,0)

    results = d.spi([0x00, 0])
    inByte1 = results['SPIBytes'][0]
    inByte2 = results['SPIBytes'][1]
    results = d.spi([0x00, 0])
    inByte3 = results['SPIBytes'][0]

    # print(inByte1, end=', ')
    # print(inByte2, end=', ')
    # print(inByte3)

    print (convert(inByte2, inByte3))

    d.setDOState(4,1)

    time.sleep(.01)
    