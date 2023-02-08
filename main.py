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

def color_processing(top_bottom_leds, left_right_leds, image_arr):
    top_colors = []
    bottom_colors = []
    left_colors = []
    right_colors = []
    (horizontal, vertical, RGB) = image_arr.shape
    hor_square_dims = horizontal/top_bottom_leds
    ver_square_dims = vertical/left_right_leds

    for i in range(top_bottom_leds):
        
        image_slice = image_arr[]


# for i in range(10):
#     image = pyautogui.screenshot()
#     image_arr = np.array(image)
#     dims = image_arr.shape
#     avg_color_row = np.average(image_arr, axis=0)
#     avg_color  = np.average(avg_color_row, axis=0)
#     avg_color_img = np.ones((1920, 1080, 3), dtype=np.uint8)
#     avg_color_img[:,:] = avg_color 
#     plt.imshow(avg_color_img)
#     plt.axis('off')
#     plt.show()

#     time.sleep(3)
    


image = pyautogui.screenshot()
image_arr = np.array(image)
print(image_arr.shape)
image_arr = image_arr[0:99,0:99,:]
print(image_arr.shape)
plt.imshow(image_arr)
plt.axis('off')
plt.show()