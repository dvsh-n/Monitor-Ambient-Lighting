import numpy as np
import pyautogui
import imutils
import cv2
from matplotlib import pyplot as plt
import time

# PC screen dims = (1080,1920,3) 
# Monitor Screen dims = (1440, 2560, 3)

# Total number of LEDs
top_bottom_leds = 10
left_right_leds = 5

def screenshot():
    image = pyautogui.screenshot()
    image = np.array(image)
    return image, image.shape

def plot(image, axis = 'off'):
    plt.imshow(image)
    plt.axis(axis)
    plt.show()    

def avg_color_img(avg_color, dims = (100, 100, 3)):
    avg_color_img = np.ones(dims, dtype=np.uint8)
    avg_color_img[:,:] = avg_color 
    return avg_color_img

def avg_color(image):
    avg_color_row = np.average(image, axis=0)
    avg_color  = np.average(avg_color_row, axis=0)       
    return avg_color


def slicing_img(top_bottom_leds, left_right_leds, image_arr):
    slices = [[], [], [], []] # 0:top 1:bottom 2:left 3:right

    (vertical, horizontal, _) = image_arr.shape
    hor_square_dims = horizontal//top_bottom_leds
    ver_square_dims = vertical//left_right_leds

    for i in range(top_bottom_leds):
        top_image_slice = image_arr[0:hor_square_dims,(i*hor_square_dims):((i+1)*hor_square_dims),:]
        slices[0].append(top_image_slice)
        bottom_image_slice = image_arr[(vertical-hor_square_dims):vertical,(i*hor_square_dims):((i+1)*hor_square_dims),:]
        slices[1].append(bottom_image_slice)
    
    for i in range(left_right_leds):
        left_image_slice = image_arr[(i*ver_square_dims):((i+1)*ver_square_dims),0:ver_square_dims,:]
        slices[2].append(left_image_slice)
        right_image_slice = image_arr[(i*ver_square_dims):((i+1)*ver_square_dims),(horizontal-ver_square_dims):horizontal,:]
        slices[3].append(right_image_slice)

    return slices

# image_arr, dims = screenshot()
# slices = slicing_img(top_bottom_leds, left_right_leds, image_arr)
# print(len(slices)) #4


