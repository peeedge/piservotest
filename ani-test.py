from __future__ import print_function
#enter the amount of data points you want then from which AIN pins you want them from, all seperated by a space
import u6
import time
import sys


dataPoints = int(sys.argv[1])
d =u6.U6()
d.getCalibrationData()
Channel = []
Gain = []
Resolution = []
Settling = []
#print(len(sys.argv))

for r in xrange(2, len(sys.argv)):
	#print(r)
	Channel.append(int(sys.argv[r]))
	Gain.append(0)
	Resolution.append(12)
	Settling.append(0)

feedbackArguments = []
print('Time, PT1-Pin {0}, PT2-pin {1}, PT3-Pin {2}, PT4-Pin {3}'.format(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]))
for i in xrange(len(sys.argv) - 2):
   feedbackArguments.append(u6.AIN24(PositiveChannel=Channel[i], ResolutionIndex=Resolution[i], GainIndex=Gain[i], SettlingFactor=Settling[i]))
#print feedbackArguments
for x in xrange(1, dataPoints):
	time.sleep(.01)
	ainBits = d.getFeedback(feedbackArguments)
	print(time.clock(), end=',')
	for e in xrange(0, len(sys.argv)-2, 4):
		print(d.binaryToCalibratedAnalogVoltage(0, ainBits[e], is16Bits = False, resolutionIndex = 0), end=',')
		print(d.binaryToCalibratedAnalogVoltage(0, ainBits[e+1], is16Bits = False, resolutionIndex = 0), end=',')
		print(d.binaryToCalibratedAnalogVoltage(0, ainBits[e+2], is16Bits = False, resolutionIndex = 0), end=',')
		print(d.binaryToCalibratedAnalogVoltage(0, ainBits[e+3], is16Bits = False, resolutionIndex = 0)) 
#print(ainBits)
