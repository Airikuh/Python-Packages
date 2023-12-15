#Crop
import cv2
import numpy as np
import matplotlib.pyplot as plt
path = r'C:\Users\airik\OneDrive\Desktop\flower.jpg'
x1 = cv2.imread(path)
x1 = cv2.cvtColor(x1, cv2.COLOR_BGR2RGB)
size_x, size_y, _ = x1.shape
#2.i: Crop
x5 = x1[int(size_x*0.25):int(size_x*0.75),int(size_y*0.25):int(size_y*0.75)]
#2.j: display to screen
plt.subplot(1, 2, 1)
plt.imshow(x5)
plt.title('x5')
