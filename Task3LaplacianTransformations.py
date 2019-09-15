import numpy as np
import cv2

image = cv2.imread('images/task1contrast.jpg')

#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

imageLaplacian = cv2.Laplacian(image, cv2.CV_64F)
imageLaplacian3 = cv2.Laplacian(image, cv2.CV_64F, 3)
imageLaplacian5 = cv2.Laplacian(image, cv2.CV_64F, 5)
imageLaplacian7 = cv2.Laplacian(image, cv2.CV_64F, 7)
imageLaplacian21= cv2.Laplacian(image, cv2.CV_64F, 21)


cv2.imwrite('images/task2Laplacian_res.jpg', imageLaplacian)
cv2.imwrite('images/task2Laplacian3_res.jpg', imageLaplacian3)
cv2.imwrite('images/task2Laplacian5_res.jpg', imageLaplacian5)
cv2.imwrite('images/task2Laplacian7_res.jpg', imageLaplacian7)
cv2.imwrite('images/task2Laplacian21_res.jpg', imageLaplacian21)