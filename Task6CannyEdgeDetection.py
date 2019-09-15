import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/dancers1.jpg', 0)
# img = cv2.imread('images/dancers.jpg', 0)
# img = cv2.imread('images/dansers2.jpg', 0)
# img = cv2.imread('images/dancers3.jpg', 0)
# img = cv2.imread('images/latinskie-tantsy2.jpg', 0)
# img = cv2.imread('images/orig.jpeg', 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
