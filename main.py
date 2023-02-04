import numpy as np
import pyautogui
import imutils
import cv2
from matplotlib import pyplot as plt
import time

for i in range(10):
    image = pyautogui.screenshot()
    image_arr = np.array(image)
    dims = image_arr.shape
    avg_color_row = np.average(image_arr, axis=0)
    avg_color  = np.average(avg_color_row, axis=0)
    avg_color_img = np.ones((1920, 1080, 3), dtype=np.uint8)
    avg_color_img[:,:] = avg_color 
    plt.imshow(avg_color_img)
    plt.axis('off')
    plt.show()

    time.sleep(3)
    


