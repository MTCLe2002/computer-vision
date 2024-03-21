import numpy as np
import cv2
import scipy.signal

I = cv2.VideoCapture(0)
Hx = np.array([[0, 1], [-1, 0]])
Hy = np.array([[-1, 0], [0, 1]])
while True:
    Status, Frame = I.read()
    gray = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
    # IxHx = cv2.filter2D(Frame, -1, Hx)
    # IxHy = cv2.filter2D(Frame, -1, Hy)
    IxHx = scipy.signal.convolve(gray, Hx, mode="same", method="direct")
    IxHy = scipy.signal.convolve(gray, Hy, mode="same", method="direct")
    A = (IxHx + IxHy).astype(np.uint8)
    cv2.imshow("thanh", A)
    if cv2.waitKey(1) == ord("q"):
        break

# cam = cv2.imread(I)
# cv2.imshow("anh", cam)
# cv2.waitKey(0)
