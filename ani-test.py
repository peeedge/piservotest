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
print(len(sys.argv))

for r in xrange(2, len(sys.argv)):
	print(r)
	Channel.append(int(sys.argv[r]))
	Gain.append(0)
	Resolution.append(12)
	Settling.append(0)

feedbackArguments = []
for i in xrange(len(sys.argv) - 2):
   feedbackArguments.append(u6.AIN24(PositiveChannel=Channel[i], ResolutionIndex=Resolution[i], GainIndex=Gain[i], SettlingFactor=Settling[i]))
#print feedbackArguments
for x in xrange(1, dataPoints):
	time.sleep(.01)
	ainBits = d.getFeedback(feedbackArguments)
	for e in xrange(len(sys.argv)-2):
		print(sys.argv[e+2], end=': ')
		print(d.binaryToCalibratedAnalogVoltage(0, ainBits[e], is16Bits = False, resolutionIndex = 0)) 
#print(ainBits)
