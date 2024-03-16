import numpy as np
import cv2

I = cv2.imread(
    r"C:\Users\mtcle\OneDrive\WorkSpace\computer-vision\data\external\image\MTCLe2002.jpg",
    0,
)
Hx = np.array([[0, 1], [-1, 0]])
Hy = np.array([[-1, 0], [0, 1]])

IxHx = cv2.filter2D(I, -1, Hx)
IxHy = cv2.filter2D(I, -1, Hy)
# Calculate the magnitude and direction of gradient using  Robert
A = IxHx + IxHy
cv2.imshow("anhBien", A)
cv2.waitKey(0)
