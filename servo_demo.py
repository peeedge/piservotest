#!/usr/bin/env python

# servo_demo.py
# 2016-10-07
# Public Domain

# servo_demo.py          # Send servo pulses to GPIO 4.
# servo_demo.py 23 24 25 # Send servo pulses to GPIO 23, 24, 25.

import sys
import time
import pigpio

MIN_WIDTH=775
MAX_WIDTH=2175

SERVO_PIN=3

width = MIN_WIDTH

pi = pigpio.pi()

if not pi.connected:
   exit()

while True:

   try:
      pi.set_servo_pulsewidth(SERVO_PIN, width)

      # print(g, width[g])

      if width<MIN_WIDTH:
         width = MIN_WIDTH
      else if width>MAX_WIDTH:
         width = MAX_WIDTH

      time.sleep(0.1)

   except KeyboardInterrupt:
      break

print("\nMoving to min")
pi.set_servo_pulsewidth(SERVO_PIN, MIN_WIDTH)

pi.stop()

