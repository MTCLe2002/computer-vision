import cv2
import scipy.signal
import numpy as np
import pandas as pd

cap = cv2.VideoCapture(0)
while True:
    # take each frame
    _, Frame = cap.read()

    # convert BRG to HSV
    hsv = cv2.cvtColor(Frame, cv2.COLOR_BGR2HSV)

    #  define range of color blue in HSV
    lower_blue = np.array([90, 50, 70])
    upper_blue = np.array([135, 255, 255])

    #  define range of color red in HSV
    lower_red = np.array([160, 50, 50])
    upper_red = np.array([180, 255, 255])

    #  define range of color red 1 in HSV
    lower_red_1 = np.array([0, 50, 50])
    upper_red_1 = np.array([30, 255, 255])

    # fine the red color red in image
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    res_red = cv2.bitwise_and(Frame, Frame, mask=mask_red)

    # fine the red 1 color red in image
    mask_red_1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
    res_red_1 = cv2.bitwise_and(Frame, Frame, mask=mask_red_1)
    # fine all red
    res_red_all = cv2.bitwise_or(res_red, res_red_1)

    #  find the blue color in image
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(Frame, Frame, mask=mask)

    res_all = cv2.bitwise_or(res_red_all, res)
    cv2.imshow(winname="frame", mat=res_red_all)
    if cv2.waitKey(1) == ord("q"):
        break
