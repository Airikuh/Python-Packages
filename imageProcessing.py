import numpy as np
import matplotlib.pyplot as plt
#2.a, read in image file and store as NumPy array
path = r'C:\Users\airik\OneDrive\Desktop\flower.jpg'
x1 = cv2.imread(path)
#2.b, Display x1
window_name = 'Flower'
cv2.imshow(window_name, x1)
#display below
#plt.imshow(x1)
#x11 = cv2.cvtColor(x1, cv2.COLOR_BGR2RGB)
x1 = cv2.cvtColor(x1, cv2.COLOR_BGR2RGB)
plt.subplot(1, 2, 1)
plt.imshow(x1)
plt.title('x1')
cv2.imwrite('x1.png', x1)
#Need explicit close or image errors out when trying to display to screen
cv2.waitKey(0)
cv2.destroyAllWindows()
#2.c, Convert the NumPy array x1 to a gray image x2
x2 =cv2.cvtColor(x1, cv2.COLOR_BGR2GRAY)
#2.d, Display x2
cv2.imshow('Gray', x2)
#display below
#plt.imshow(x2)
#Need explicit close or image errors out when trying to display to screen
cv2.waitKey(0)
cv2.destroyAllWindows()
#2.e, Rotate x1 clockwise by 90 degrees and save the result in x3
x3 = cv2.rotate(x2, cv2.ROTATE_90_CLOCKWISE)
#2.f, Display x3 below
#plt.imshow(x3)
#2.f, Display x3 to screen
cv2.imshow('Rotate', x3)
#Need explicit close or image errors out when trying to display to screen
cv2.waitKey(0)
cv2.destroyAllWindows()
#2.g, Scale down x1 to its half size, and save the result in x4
height, width = x1.shape[:2]
print('Height: ', height)
print('Width: ', width)
x4 = cv2.resize(x1, (330, 500))
#2.i, Crop x1 around its centroid such that the cropped window has a half of its original width
and height. Save the cropped image as x5
size_x, size_y, _ = x1.shape
#x5 = x1[int(size_x*0.50):int(size_x*0.50),int(size_y*0.50):int(size_y*0.50)]
#2.j, Display x5
#cv2.imshow('Cropped', x5)
#Need explicit close or image errors out when trying to display to screen
cv2.waitKey(0)
cv2.destroyAllWindows()

