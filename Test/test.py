import serial

def port(COM):
    return serial.Serial(COM, 115200, timeout=1)

def write_ser_int(port, data, num_bytes_return = False):
    num_bytes = port.write(bytearray(data))
    if num_bytes_return: return num_bytes

def read_ser(port, buffer = 255):
    string = port.read(buffer)
    return string

def check_port(COM):
    if COM.isOpen():
        print("port is open")
    else:
        print("port open failed")

Arduino = port("COM8")
check_port(Arduino)

Arduino.write(bytearray([20,40,200,30,45,120,90,20,10,200,210,0]))
print("done")
Arduino.close()

# while(1): # loop runs when serial data is received
#     if Arduino.in_waiting:
#         result = read_ser(Arduino)
#         # if result == b'bgn':
#         #     Arduino.write([57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57])
#         print(result)
#         Arduino.flush()


# Serial.in_waiting returns the number of bytes in the input buffer
# val = str(input("Here:"))
# print(val.encode())
