import numpy as np
import cv2

image = cv2.imread('images/task1contrast.jpg')

imageGauss = cv2.GaussianBlur(image, (55, 55), 0)
imageGauss2 = cv2.GaussianBlur(image, (0, 0), 25, 25)
imageGaussX = cv2.GaussianBlur(image, (0, 0), 15, 1, cv2.BORDER_WRAP)
imageGaussY = cv2.GaussianBlur(image, (0, 0), 5, 15, cv2.BORDER_REPLICATE)

cv2.imwrite('images/task2Gauss_res.jpg', imageGauss)
cv2.imwrite('images/task2Gauss_res2.jpg', imageGauss2)
cv2.imwrite('images/task2Gauss_resX.jpg', imageGaussX)
cv2.imwrite('images/task2Gauss_resY.jpg', imageGaussY)


