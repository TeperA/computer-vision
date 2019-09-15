import numpy as np
import cv2

image = cv2.imread('images/task1contrast.jpg')

imageBilateral = cv2.bilateralFilter(image, 5, 5, 80)
imageBilateral2 = cv2.bilateralFilter(image, 5, 80, 5)
imageBilateral3 = cv2.bilateralFilter(image, 5, 5, 5)
imageBilateral4 = cv2.bilateralFilter(image, 5, 80, 80)

cv2.imwrite('images/task2Bilateral_res.jpg', imageBilateral)
cv2.imwrite('images/task2Bilateral_res2.jpg', imageBilateral2)
cv2.imwrite('images/task2Bilateral_res3.jpg', imageBilateral3)
cv2.imwrite('images/task2Bilateral_res4.jpg', imageBilateral4)


