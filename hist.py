import cv2
from matplotlib import pyplot as plt

#  img = cv2.imread('images/task1contrast.jpg', 0)

img = cv2.imread('images/dancers.jpg', 0)

equ = cv2.equalizeHist(img)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(equ, cmap='gray')
plt.title('Histogram Equalization'), plt.xticks([]), plt.yticks([])

plt.show()
