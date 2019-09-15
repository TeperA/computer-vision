import numpy as np
import cv2

image = cv2.imread('images/task1contrast.jpg')

imageMedian = cv2.medianBlur(image, 5)
imageMedian2 = cv2.medianBlur(image, 15)
imageMedian3 = cv2.medianBlur(image, 25)
imageMedian4 = cv2.medianBlur(image, 55)

cv2.imwrite('images/task2Median_res.jpg', imageMedian)
cv2.imwrite('images/task2Median_res2.jpg', imageMedian2)
cv2.imwrite('images/task2Median_res3.jpg', imageMedian3)
cv2.imwrite('images/task2Median_res4.jpg', imageMedian4)


