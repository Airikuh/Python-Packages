import cv2
import numpy as np
import matplotlib.pyplot as plt
path = r'C:\Users\airik\OneDrive\Desktop\flower.jpg'
x1 = cv2.imread(path)
#Displays below with correct color! Else is a blue rose
x1 = cv2.cvtColor(x1, cv2.COLOR_BGR2RGB)
plt.subplot(1, 2, 1)
plt.imshow(x1)
plt.title('x1')
#2.c, Convert the NumPy array x1 to a gray image x2
x2 =cv2.cvtColor(x1, cv2.COLOR_BGR2GRAY)
print(x2.shape)
#2.d, Display x2
#cv2.imshow('Gray', x2)
plt.subplot(1, 2, 1)
plt.imshow(x2, cmap='gray')
#plt.imshow(x2)
plt.title('x2')
