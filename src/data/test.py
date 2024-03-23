import numpy as np
import cv2

# import scipy.signal
from scipy.signal import convolve

image = cv2.imread(
    r"C:\Users\mtcle\OneDrive\WorkSpace\computer-vision\data\external\image\sieunhan.png"
)
###binarising
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret2, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
Hx = np.array([[0, 1], [-1, 0]]).astype(np.uint8)

Hy = np.array([[-1, 0], [0, 1]]).astype(np.uint8)
IxHx = convolve(gray, Hx, mode="valid")
IxHy = convolve(gray, Hy, mode="valid")
# Calculate the magnitude and direction of gradient using  Robert
A = IxHx + IxHy
B, _ = cv2.findContours(A, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(B)
