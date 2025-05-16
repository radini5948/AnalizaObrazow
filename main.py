import cv2
from matplotlib import pyplot as plt
import numpy as np
img1 = cv2.imread("1n_00.jpg", cv2.IMREAD_COLOR)
img2 = cv2.imread("1xn_180.jpg", cv2.IMREAD_COLOR)
img1 = np.array(255*(img1/255)**1, dtype='uint8')
img2 = np.array(255*(img2/255)**1, dtype='uint8')
img3 = cv2.hconcat([img1,img2])
N1 = 23
N2 = 9

blurred_img2 = cv2.GaussianBlur(img1, (N2, N2), N2/3)
b,g,r = cv2.split(blurred_img2)
k = np.zeros_like(b)

r_eq = cv2.equalizeHist(r)
g_eq = cv2.equalizeHist(g)
b_eq = cv2.equalizeHist(b)

r1 = cv2.medianBlur(r_eq, 7)
g1 = cv2.medianBlur(g_eq, 7)
b1 = cv2.medianBlur(b_eq, 7)
a = cv2.merge([b1,g1,r1])
cv2.imshow("image", a)
bin1 = ((g1 - b1) > 10) & (abs(g1 - r1) > 5) & (r1 < 200) & (g1 < 215) & (b1 < 190) & (abs(r1 - b1) < 35)

cv2.imshow("Binary Image", bin1.astype(np.uint8) * 255)
cv2.waitKey(0)
