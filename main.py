import numpy as np
import pyautogui
import imutils
import cv2

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
print(image.shape)
cv2.imwrite("in_memory_to_disk.png", image)