#Rotate and Display
import cv2
import numpy as np
import matplotlib.pyplot as plt
path = r'C:\Users\airik\OneDrive\Desktop\flower.jpg'
x1 = cv2.imread(path)
x1 = cv2.cvtColor(x1, cv2.COLOR_BGR2RGB)
#2.e: Rotate x1 by 90 degrees
x3 = cv2.rotate(x1, cv2.ROTATE_90_CLOCKWISE)
#2.f: display to screen
plt.subplot(1, 2, 1)
plt.imshow(x3)
plt.title('x3')
