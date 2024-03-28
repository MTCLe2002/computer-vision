import cv2
from matplotlib.pyplot import gray
import numpy as np

img = cv2.imread(
    r"C:\Users\mtcle\OneDrive\WorkSpace\computer-vision\data\external\image\Arduino_Uno.jpg"
)
imgrs = cv2.resize(img, (500, 374))
gray = cv2.cvtColor(imgrs, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey()
