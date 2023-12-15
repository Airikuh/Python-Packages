import cv2
import matplotlib.pyplot as plt

#edited here
path = r'C:\Users\Airikuh\Desktop\Island.png'

# In cv2, a RGB image is read as a BGR array
img_bgr = cv2.imread(path) 

img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

plt.subplot(1, 2, 1)
plt.imshow(img_bgr)	
plt.title('img_bgr')

plt.subplot(1,2, 2)
plt.imshow(img_rgb)
plt.title('img_rgb')

# In cv2, a BGR array is written as a RGB image
cv2.imwrite('img_bgr.png', img_bgr)
cv2.imwrite('img_rgb.png', img_rgb)
 
