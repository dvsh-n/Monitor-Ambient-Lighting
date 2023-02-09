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


def color_processing(top_bottom_leds, left_right_leds, image_arr):
    top_colors = []
    bottom_colors = []
    left_colors = []
    right_colors = []
    (vertical, horizontal, RGB) = image_arr.shape
    hor_square_dims = horizontal//top_bottom_leds
    ver_square_dims = vertical//left_right_leds

    for i in range(top_bottom_leds):
        top_image_slice = image_arr[0:hor_square_dims,(i*hor_square_dims):((i+1)*hor_square_dims),:]
        top_colors.append(avg_color(top_image_slice))
        bottom_image_slice = image_arr[(vertical-hor_square_dims):vertical,(i*hor_square_dims):((i+1)*hor_square_dims),:]
        bottom_colors.append(avg_color(bottom_image_slice))

    return top_colors

time.sleep(3)
image, dims = screenshot()
colors = color_processing(top_bottom_leds=top_bottom_leds, left_right_leds=left_right_leds, image_arr=image)
for i in range(top_bottom_leds):
    plot(avg_color_img(colors[i]))


