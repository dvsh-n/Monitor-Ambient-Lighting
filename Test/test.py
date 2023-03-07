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

Arduino = port("COM14")
check_port(Arduino)

while(1):
    val = str(input("Here:"))
    print(val.encode())
    Arduino.write([90, 57, 57])
    print(read_ser(Arduino))
