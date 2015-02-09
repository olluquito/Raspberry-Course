#!/usr/bin/env python
import serial
ser = serial.Serial('/dev/ttyAMA0', 9600)
ser.write('some text')
while True:
    print(ser.read())
