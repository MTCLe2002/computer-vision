import cv2
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

img = cv2.imread(
    r"C:\Users\mtcle\OneDrive\WorkSpace\computer-vision\data\external\image\sieunhan.png",
    0,
)
H1 = np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]])
H2 = np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]])
H3 = np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]])
H4 = np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]])
H5 = np.array([[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]])
H6 = np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]])
H7 = np.array([[-3, -3, -3], [5, 0, -3], [5, 5, -3]])
H8 = np.array([[5, -3, -3], [5, 0, -3], [5, -3, -3]])
A1 = scipy.signal.convolve(img, H1, mode="same", method="auto")
A2 = scipy.signal.convolve(img, H2, mode="same", method="auto")
A3 = scipy.signal.convolve(img, H3, mode="same", method="auto")
A4 = scipy.signal.convolve(img, H4, mode="same", method="auto")
A5 = scipy.signal.convolve(img, H5, mode="same", method="auto")
A6 = scipy.signal.convolve(img, H6, mode="same", method="auto")
A7 = scipy.signal.convolve(img, H7, mode="same", method="auto")
A8 = scipy.signal.convolve(img, H8, mode="same", method="auto")
M1 = np.maximum(A1, A2)
M2 = np.maximum(M1, A3)
M3 = np.maximum(M2, A4)
M4 = np.maximum(M3, A5)
M5 = np.maximum(M4, A6)
M6 = np.maximum(M5, A7)
M7 = np.maximum(M6, A8)
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("anh goc")
plt.subplot(122)
plt.imshow(M7, cmap="gray")
plt.title("anh tach bien kirsch")
plt.show()
cv2.waitKey()
