import cv2
import matplotlib.pyplot as plt
import numpy as np

path_bgr = r'C:\Users\Airikuh\Desktop\img_bgr.png'
path_rgb = r'C:\Users\Airikuh\Desktop\img_rgb.png'

img_bgr = cv2.imread(path_bgr) 
img_rgb = cv2.imread(path_rgb) 

img_bgr_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
img_rgb_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

print(img_bgr.shape) 
print(img_rgb_gray.shape)

plt.subplot(1, 2, 1) 
plt.imshow(img_bgr_gray, cmap='gray') 
plt.title('img_bgr_gray')

plt.subplot(1,2, 2) 
plt.imshow(img_rgb_gray, cmap='gray') 
plt.title('img_rgb_gray')

cv2.imwrite('img_bgr_gray.png', img_bgr_gray)
cv2.imwrite('img_rgb_gray.png', img_rgb_gray)

t = cv2.imread('img_bgr_gray.png')
print(t.shape)
s = cv2.imread('img_bgr_gray.png',0)
print(s.shape)

cv2.imshow('gray', img_bgr_gray) 
cv2.waitKey(0)
