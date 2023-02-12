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


def slicing_img(top_bottom_leds, left_right_leds, image_arr, extra_slice = (0, 0), slices = False): # extra_slice = (# extra vert px for hor, # extra hor px for vert)
    if slices:
       slices = [[], [], [], []] # 0:top 1:bottom 2:left 3:right
    colors = [[], [], [], []]

    (vertical, horizontal, _) = image_arr.shape
    hor_scn_sqr_dims = horizontal//top_bottom_leds 
    ver_scn_sqr_dims = vertical//left_right_leds + extra_slice[1]

    for i in range(top_bottom_leds):
        top_image_slice = image_arr[0:(hor_scn_sqr_dims+extra_slice[0]), # vertical
                                    (i*hor_scn_sqr_dims):((i+1)*hor_scn_sqr_dims), #horizontal
                                    :]
        if slices: slices[0].append(top_image_slice)
        colors[0].append(avg_color(top_image_slice))

        bottom_image_slice = image_arr[(vertical-(hor_scn_sqr_dims+extra_slice[0])):vertical, # vertical
                                        (i*hor_scn_sqr_dims):((i+1)*hor_scn_sqr_dims), # horizontal
                                        :]
        if slices: slices[1].append(bottom_image_slice)
        colors[1].append(avg_color(bottom_image_slice))
    
    for i in range(left_right_leds):
        left_image_slice = image_arr[(i*ver_scn_sqr_dims):((i+1)*ver_scn_sqr_dims), # vertical 
                                    0:(ver_scn_sqr_dims+extra_slice[1]), # horizontal
                                    :]
        if slices: slices[2].append(left_image_slice)
        colors[2].append(avg_color(left_image_slice))

        right_image_slice = image_arr[(i*ver_scn_sqr_dims):((i+1)*ver_scn_sqr_dims), # vertical 
                                        (horizontal-(ver_scn_sqr_dims+extra_slice[1])):horizontal, # horizontal
                                        :]
        if slices: slices[3].append(right_image_slice)
        colors[3].append(avg_color(right_image_slice))

    return slices

def color_from_slices(slices):
    colors = [[], [], [], []]
    for i in range(len(slices)):
        for j in range(len(slices[i])):
            colors[i][j] = avg_color(slices[i][j])
            print(0)
    return colors

t1 = time.time()
image_arr, dims = screenshot()
slices = slicing_img(top_bottom_leds, left_right_leds, image_arr)
colors = color_from_slices(slices)
t2 = time.time()
print(t2-t1)


