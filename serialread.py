import serial
import sys

ser = serial.Serial('/dev/tty.usbmodem1431')
print(ser.name)

logfile = open("result.txt", "w")

for x in xrange(1,100):
	line = ser.readline()
	sys.stdout.write(line)
	logfile.write(line)

logfile.close()
ser.close()