import numpy as np
import cv2
from matplotlib import pyplot as plt

# img1 = cv2.imread('box.png', 0)         # queryImage
# img2 = cv2.imread('box_in_scene.png', 0)# trainImage
img1 = cv2.imread('images/grechka.jpg', 0)       # queryImage
img2 = cv2.imread('images/grechka-clip.jpg', 0)  # trainImage
img4 = cv2.imread('images/hpof.jpg', 0)
img5 = cv2.imread('images/hp-books.jpg', 0)
img7 = cv2.imread('images/chai.jpg', 0)
img8 = cv2.imread('images/chaidoma2.jpg', 0)
img10 = cv2.imread('images/key.jpg', 0)       # queryImage
img11 = cv2.imread('images/keys.jpg', 0)  # trainImage

# Initiate SIFT detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT

#  kp1, des1 = orb.detectAndCompute(img1, None)
#  kp2, des2 = orb.detectAndCompute(img2, None)
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
kp4, des4 = orb.detectAndCompute(img4, None)
kp5, des5 = orb.detectAndCompute(img5, None)
kp7, des7 = orb.detectAndCompute(img4, None)
kp8, des8 = orb.detectAndCompute(img5, None)
kp10, des10 = orb.detectAndCompute(img10, None)
kp11, des11 = orb.detectAndCompute(img11, None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1, des2)

# Sort them in the order of their distance.
matches = sorted(matches, key=lambda x: x.distance)


#  draw_params = dict(matchColor=(0, 255, 0), singlePointColor=(255, 0, 0), matchesMask=matchesMask, flags=0)

#  Draw first 20 matches.
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:20], None, flags=2)
img6 = cv2.drawMatches(img4, kp4, img5, kp5, matches[:20], None, flags=2)
img9 = cv2.drawMatches(img7, kp7, img8, kp8, matches[:50], None, flags=2)
img12 = cv2.drawMatches(img10, kp10, img11, kp11, matches[:50], None, flags=2)

#  plt.imshow(img3), plt.show()
#  plt.imshow(img6), plt.show()
plt.imshow(img12), plt.show()
