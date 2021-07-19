import serial
import binascii
import time

def serial_read(ser):
    time.sleep(0.3)
    data = bytearray()  # empty array for received bytes
    while True:  # execute this until bytes received on serial buffer
        bytes_to_read = ser.inWaiting()
        if bytes_to_read > 0:
            time.sleep(0.3)
            break
    for i in range(bytes_to_read):
        data += bytearray(ser.read())  # fill the byte array with received bytes sequentially
    return data
