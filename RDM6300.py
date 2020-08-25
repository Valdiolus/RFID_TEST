import time
import serial
import numpy as np

def TTY_INIT(tty, speed):
    ser = serial.Serial()
    ser.port = tty #"/dev/ttyUSB0" #ttyACM0"
    ser.baudrate = speed
    #ser.NewLine = "\n"
    ser.open()
    return ser

ser = TTY_INIT("/dev/ttyUSB0", 9600)
buffer = [0,0,0,0,0,0,0,0,0,0]
checksum = [0,0]
stage=0

while(1):
    byte = ser.read()
    if byte == b'\x03' and stage > 0:
        print("New packet:", buffer, checksum)
        stage = 0
        continue
    if stage > 10:
        checksum[stage-11] = byte
        continue
    if stage > 0:
        buffer[stage-1] = byte
        stage += 1
    if byte == b'\x02' and stage == 0:
        stage = 1

    #print(byte) #print(byte)#



