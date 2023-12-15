# Rotation at any angle
import cv2
import matplotlib.pyplot as plt
import imutils

path_rgb = r'C:\Users\Airikuh\Desktop\img_rgb.png'
img_rgb = cv2.imread(path_rgb) 
img5a = imutils.rotate(img_rgb, 32)  # 32 degree

plt.imshow(img5a)
