import numpy as np
# import pyautogui
# import imutils
# import cv2
from matplotlib import pyplot as plt
import time
import dxcam
from PIL import Image
import serial

# PC screen dims = (1080,1920,3) 
# Monitor Screen dims = (1440, 2560, 3)

# Total number of LEDs
top_bottom_leds = 21
left_right_leds = 12

def screenshot(cam):
    image = cam.grab()
    return image, image.shape

def plot(image, axis = 'off'):
    plt.imshow(image)
    plt.axis(axis)
    plt.show()    

def avg_color_img(avg_color, dims = (100, 100, 3)):
    avg_color_img = np.ones(dims, dtype=np.uint8)
    avg_color_img[:,:] = avg_color 
    return avg_color_img

def avg_color(image, type_char = True):
    avg_color_row = np.average(image, axis=0)
    avg_color  = np.average(avg_color_row, axis=0)     
    avg_color = np.floor(avg_color)
    if type_char: avg_color[0], avg_color[1], avg_color[2] = chr(avg_color[0]), chr(avg_color[1]), chr(avg_color[2])
    return avg_color


def colors_from_img(top_bottom_leds, left_right_leds, image, extra_slice = (0, 0)): # extra_slice = (# extra vert px for hor, # extra hor px for vert)
    colors = [[], [], [], []]# 0:top 1:bottom 2:left 3:right

    (vertical, horizontal, _) = image.shape
    hor_scn_sqr_dims = horizontal//top_bottom_leds 
    ver_scn_sqr_dims = vertical//left_right_leds + extra_slice[1]

    for i in range(top_bottom_leds):
        top_image_slice = image[0:(hor_scn_sqr_dims+extra_slice[0]), # vertical
                                    (i*hor_scn_sqr_dims):((i+1)*hor_scn_sqr_dims), #horizontal
                                    :]
        colors[0].append(avg_color(top_image_slice))

        bottom_image_slice = image[(vertical-(hor_scn_sqr_dims+extra_slice[0])):vertical, # vertical
                                        (i*hor_scn_sqr_dims):((i+1)*hor_scn_sqr_dims), # horizontal
                                        :]
        colors[1].append(avg_color(bottom_image_slice))
    
    for i in range(left_right_leds):
        left_image_slice = image[(i*ver_scn_sqr_dims):((i+1)*ver_scn_sqr_dims), # vertical 
                                    0:(ver_scn_sqr_dims+extra_slice[1]), # horizontal
                                    :]
        colors[2].append(avg_color(left_image_slice))

        right_image_slice = image[(i*ver_scn_sqr_dims):((i+1)*ver_scn_sqr_dims), # vertical 
                                        (horizontal-(ver_scn_sqr_dims+extra_slice[1])):horizontal, # horizontal
                                        :]
        colors[3].append(avg_color(right_image_slice))

    return colors
def black_border_crop(image):
    avg_color_col = np.average(image, axis=1)



def port(COM):
    return serial.Serial(COM, 921600, timeout=1)

def write_ser(port, data, num_bytes_return = False):
    # data += '\n'
    num_bytes = port.write(data.encode())
    if num_bytes_return: return num_bytes

def read_ser(port, buffer = 255):
    string = port.read(buffer)
    return string.decode()

def check_port(COM):
    if COM.isOpen():
        print("port is open")
    else:
        print("port open failed")

def send(port, colors, order = [1, 2, 0, 3]):
    for i in order:
        for j in colors[i]:
            for k in j:
                write_ser(port, k)


ESP32 = port("COM9")
check_port(ESP32)

while(1):
    string = read_ser(ESP32)
    if (len(string)):
        print(string)
    
    cmd = input()
    if (cmd):
        write_ser(ESP32, cmd)


# camera = dxcam.create(device_idx=0, output_idx=1)
# t1 = time.time()
# image, dims = screenshot(camera)
# colors = colors_from_img(top_bottom_leds, left_right_leds, image)
# t2 = time.time()
# print(1/(t2-t1))
# Image.fromarray(image).show()
# serial is very fast, no need to worry abot speed
# baud rate is bits per second
# topleds ~ 21
# sideleds ~ 12
# cout << +c; can be used to convert char to int