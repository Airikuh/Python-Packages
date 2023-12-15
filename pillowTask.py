import PIL
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
#5.a Use PIL.Image.open to open the image file: flower.jpg and store it in an image object y1
y1 = Image.open(r'C:\Users\airik\OneDrive\Desktop\flower.jpg')
#5.b Display y1
y1.show()
#5.c Rotate y1 by 25 degree with expand = 1 and save the result as another image object y2
y2 = y1.rotate(25, expand=1)
#others have expand as True, might be a problem
#5.d Display the width and height of y2
width, height = y2.size
print('The Width of y2: ', width)
print('The Height of y2: ', height)
#5.e Let left, top, right, bottom = 4, height/5, width/2, 3*height/5
#sets the points for the cropped image
left = 4
top = height/5
right = width/2
bottom = 3*height/5
#5.f use (left, top, right, bottom) to crop y1 and save the result as an image object y3
y3 = y1.crop((left, top, right, bottom))
#5.g Display y3
y3.show()
#5.h let newsize = (128, 128)
newsize = (128, 128)
#5.i use newsize to resize y1 to y4
y4 = y1.resize(newsize)
#5.j save y4 as an image file: resized_image.png
y4 = y4.save('resized_image.png')
