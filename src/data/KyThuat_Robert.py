import numpy as np
import cv2
from scipy.signal import convolve2d

I = np.array(
    [
        [4, 7, 3, 7, 1],
        [5, 7, 1, 7, 1],
        [6, 6, 1, 8, 3],
        [5, 7, 5, 7, 1],
        [5, 7, 6, 1, 2],
    ]
)

print(I)
Hx = np.array([[0, 1], [-1, 0]]).astype(np.uint8)

Hy = np.array([[-1, 0], [0, 1]]).astype(np.uint8)

IxHx = convolve2d(I, Hx, mode="valid")
IxHy = convolve2d(I, Hy, mode="valid")
# Calculate the magnitude and direction of gradient using  Robert
A = IxHx + IxHy
print(A)
