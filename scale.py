import cv2
import matplotlib.pyplot as plt
import numpy as np

# crop an image
path_rgb = r'C:\Users\Airikuh\Desktop\img_rgb.png'
img_rgb = cv2.imread(path_rgb) 
sizex, sizey, _ = img_rgb.shape
img4a = img_rgb[int(sizex*0.25):int(sizex*0.75),int(sizey*0.25):int(sizey*0.75)]
plt.imshow(img4a)
