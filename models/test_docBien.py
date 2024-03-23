import cv2
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
import sys

sys.path.append("src/data")
import Total_tachBien

img = cv2.imread(
    r"C:\Users\mtcle\OneDrive\WorkSpace\computer-vision\data\external\image\sieunhan.png"
)  # queryImage
RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
sobel = Total_tachBien.sobel(gray)
laplace = Total_tachBien.laplace(gray)
canny = cv2.Canny(gray, 100, 200)
plt.subplot(221)
plt.imshow(RGB)
plt.title("Original")
plt.subplot(222)
plt.imshow(sobel, cmap="gray")
plt.title("sobel")
plt.subplot(223)
plt.imshow(laplace, cmap="gray")
plt.title("laplace")
plt.subplot(224)
plt.imshow(canny, cmap="gray")
plt.title("canny")
plt.show()
