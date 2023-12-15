#Color Segmentation
import cv2
import numpy as np
import matplotlib.pyplot as plt
path_yellow = r'C:\Users\airik\OneDrive\Desktop\Yellow_traffic_sign.jpg'
image = cv2.imread(path_yellow)
# Converting the image to hsv
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# define range of red color in HSV
lower_yellow = np.array([15,50,180])
upper_yellow = np.array([40,255,255])
# Threshold the HSV image using inRange function to get only yellow colors
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
plt.figure(figsize=[13,13])
plt.subplot(121);plt.imshow(image[:,:,::-1]);plt.title("Original Image",fontdict={'fontsize':
25});plt.axis('off');
plt.subplot(122);plt.imshow(mask, cmap='gray');plt.title("Mask of Yellow
Color",fontdict={'fontsize': 25});plt.axis('off');
plt.show()
res = cv2.bitwise_and(image,image, mask= mask)
plt.figure(figsize=[13,13])
plt.imshow(res[:,:,::-1]);plt.title("Yellow part of the Image",fontdict={'fontsize':35});plt.axis('off');
plt.show()
