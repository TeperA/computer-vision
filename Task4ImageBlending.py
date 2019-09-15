import cv2
import numpy as np


def blend(image1, image2, height, k):
    a = cv2.imread(image1)
    b = cv2.imread(image2)

    # generate gaussian pyramid for a
    g = a.copy()
    gpa = [g]
    for i in range(height):
        g = cv2.pyrDown(g)
        gpa.append(g)

    # generate gaussian pyramid for b
    g = b.copy()
    gpb = [g]
    for i in range(height):
        g = cv2.pyrDown(g)
        gpb.append(g)

    # generate Laplacian Pyramid for a
    lpa = [gpa[height - 1]]
    for i in range(height - 1, 0, -1):
        ge = cv2.pyrUp(gpa[i])
        L = cv2.subtract(gpa[i - 1], ge)
        lpa.append(L)

    # generate Laplacian Pyramid for b
    lpb = [gpb[height - 1]]
    for i in range(height - 1, 0, -1):
        ge = cv2.pyrUp(gpb[i])
        L = cv2.subtract(gpb[i-1], ge)
        lpb.append(L)

    # Now add left and right halves of images in each level
    lS = []
    for la, lb in zip(lpa, lpb):
        rows, cols, dpt = la.shape
        ls = np.hstack((la[:, 0:int(cols / 2)], lb[:, int(cols / 2):]))
        lS.append(ls)

    # now reconstruct
    ls_ = lS[0]
    for i in range(1, height):
        ls_ = cv2.pyrUp(ls_)
        ls_ = cv2.add(ls_, lS[i])

    # image with direct connecting each half
    real = np.hstack((a[:, :int(cols / 2)], b[:, int(cols / 2):]))

    cv2.imwrite('images/Pyramid_blending' + str(k) + '.jpg', ls_)
    cv2.imwrite('images/Direct_blending' + str(k) + '.jpg', real)


#blend('images/apple.jpg', 'images/orange.jpg', 6, '_Example')
#blend('images/apple.jpg', 'images/orange.jpg', 8, '_Example8')
blend('images/watermelon.jpg', 'images/ball.jpg', 1, 1)
blend('images/watermelon.jpg', 'images/ball.jpg', 2, 2)
blend('images/watermelon.jpg', 'images/ball.jpg', 3, 3)
blend('images/watermelon.jpg', 'images/ball.jpg', 4, 4)
blend('images/watermelon.jpg', 'images/ball.jpg', 5, 5)
blend('images/watermelon.jpg', 'images/ball.jpg', 6, 6)
blend('images/watermelon.jpg', 'images/ball.jpg', 7, 7)
blend('images/watermelon.jpg', 'images/ball.jpg', 8, 8)
#blend('images/horse1.jpg', 'images/horse2.jpg', 4, '_Horses4')
#blend('images/horse1.jpg', 'images/horse2.jpg', 6, '_Horses')
#blend('images/horse1.jpg', 'images/horse2.jpg', 8, '_Horses8')
#blend('images/force3.jpg', 'images/force4.jpg', 6, '_Horses')
#blend('images/force3.jpg', 'images/force4.jpg', 8, '_Horses8')