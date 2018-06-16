#!/usr/bin/env python

import serial
import time
from sys import stdout

print("starting jrk_simple_test")
ser = serial.Serial( "/dev/ttyACM0", 9600)   # input to the JRK controller for sending it commands
print("connected to: " + ser.portstr + " for sending commands to JRK")

init_cmd = "\xAA"
jrk_id = "\x0B"
set_target_cmd = "\xC0"
stop_cmd = "\xFF"
read_feedback_cmd = "\xA5"
read_current_cmd = "\x8F"
read_scaled_feedback = "\xA7"
get_error_cmd = "\x33"

# For my John Deere tractor steering: 2400 full right; 1450 straight; 450 full left
# clear error bits and read the register; Pololu protocol: 0xAA, device number, 0x33; Reference "Get Error Flags Halting" page 34 of manual
print("Clearing errors on start up")
ser.write([init_cmd, jrk_id, get_error_cmd])
time.sleep(0.1)
cycle_delay = .1
for target in [2048, 4094, 1024, 0]:
	lowByte = (target & ord("\x1F")) | ord(set_target_cmd)
	highByte = (target >> 5) & ord("\x7F")
	ser.write([init_cmd, jrk_id, lowByte, highByte])
	time.sleep (0.01)
	for i in range(1, 30): 
		time.sleep (cycle_delay)
		ser.write([init_cmd, jrk_id, read_current_cmd])
		time.sleep (0.01)
		checkCurrent = ord(ser.read())
		ser.write([init_cmd, jrk_id, read_feedback_cmd])
		time.sleep (0.01)
		checkFeedback = (ord(ser.read()) | ord(ser.read())<<8)
		time.sleep (0.01)
		ser.write([init_cmd, jrk_id, read_scaled_feedback])
		time.sleep (0.01)
		scaled_feedback = (ord(ser.read()) | ord(ser.read())<<8)		
		#stdout.write (" \r target: %s feedback is at %s of 4095, interation %s" % (target, checkFeedback, i))  # use this if you don't want the values to scroll
		#stdout.flush() # used with the statement above
		target_delta = abs(target-scaled_feedback)
		print ("  target: %s feedback: %s scaled feedback: %s current: %s delta: %s interation %s" % (target, checkFeedback, scaled_feedback, checkCurrent, target_delta, i))	
	ser.write(stop_cmd)
	print ("- Finished.")
ser.write(stop_cmd)
