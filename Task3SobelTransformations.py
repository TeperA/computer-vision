import numpy as np
import cv2

image = cv2.imread('images/task1contrast.jpg')

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

imageSobelX = cv2.Sobel(image, cv2.CV_64F, dx=1, dy=0)
imageSobelY = cv2.Sobel(image, cv2.CV_64F, dx=0, dy=1)
imageSobelXY = cv2.Sobel(image, cv2.CV_64F, dx=1, dy=1)
imageSobel2X = cv2.Sobel(image, cv2.CV_64F, dx=2, dy=0)
imageSobel2Y = cv2.Sobel(image, cv2.CV_64F, dx=0, dy=2)

cv2.imwrite('images/task2Sobel_res1X.jpg', imageSobelX)
cv2.imwrite('images/task2Sobel_res2Y.jpg', imageSobelY)
cv2.imwrite('images/task2Sobel_res3XY.jpg', imageSobelXY)
cv2.imwrite('images/task2Sobel_res42X.jpg', imageSobel2X)
cv2.imwrite('images/task2Sobel_res52Y.jpg', imageSobel2Y)

