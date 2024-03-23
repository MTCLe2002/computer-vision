import cv2
import numpy as np
import scipy.signal

img = cv2.imread(
    r"C:\Users\mtcle\OneDrive\WorkSpace\computer-vision\data\external\image\sieunhan.png",
    0,
)
Hx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

Hy = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

A = (
    scipy.signal.convolve(img, Hx, mode="same", method="direct")
    + scipy.signal.convolve(img, Hy, mode="same", method="direct")
).astype(np.uint8)
cv2.imshow("anh", A)
cv2.waitKey()
