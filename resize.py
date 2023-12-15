import numpy as np
import matplotlib.pyplot as plt
path = r'C:\Users\airik\OneDrive\Desktop\flower.jpg'
x1 = cv2.imread(path)
x1 = cv2.cvtColor(x1, cv2.COLOR_BGR2RGB)
#2.g Scale down x1 to its half size, and save the result in x4
x4 = cv2.resize(x1, (330, 500))
# 2. H: Display
plt.subplot(1, 2, 1)
plt.imshow(x4)
plt.title('x4')
