import numpy as np
import cv2

#https://docs.opencv.org/3.3.0/de/d25/imgproc_color_conversions.html

k_a = 1.0
k_b = 1.5
k_l = 2.0

image = cv2.imread('images/task1contrast.jpg')
lab_image = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
#print(lab_image)
l, a, b = cv2.split(lab_image)
#print(l)
a1 = (a - 128.) * k_a + 128
b1 = (b - 128.) * k_b + 128

new_image = cv2.merge((l.astype(np.uint8), a1.astype(np.uint8), b1.astype(np.uint8)))
try_image = cv2.cvtColor(new_image, cv2.COLOR_LAB2RGB)
cv2.imwrite('images/task1contrast_res.jpg', try_image)

#l2 = l / alpha
l2 = np.where(l > 255/k_l, 255, l * k_l)
#print(l2)
#tmp = l * 0.5
#l2 = np.where(tmp > 100., tmp, tmp)
'''for el in l2.flat:
    if el > 100.:
        el = 100.'''
new_image_2 = cv2.merge((l2.astype(np.uint8), a.astype(np.uint8), b.astype(np.uint8)))
try_image_2 = cv2.cvtColor(new_image_2, cv2.COLOR_LAB2RGB)
cv2.imwrite('images/task1contrast_res2.jpg', try_image_2)


new_image_3 = cv2.merge((l2.astype(np.uint8), a1.astype(np.uint8), b1.astype(np.uint8)))
try_image_3 = cv2.cvtColor(new_image_3, cv2.COLOR_LAB2RGB)
cv2.imwrite('images/task1contrast_res3.jpg', try_image_3)

