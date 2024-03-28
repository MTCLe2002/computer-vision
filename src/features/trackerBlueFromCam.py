from matplotlib import contour
import numpy as np
import pandas as pd
import cv2
import scipy.signal

cap = cv2.VideoCapture(0)
while True:
    # take each frame
    _, Frame = cap.read()
    Frame = cv2.flip(Frame, 1)  # flipping
    # convert BRG to HSV
    hsv = cv2.cvtColor(Frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 70])
    upper_blue = np.array([135, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # cv2.imshow("anh", mask)
    # con là tập hợp các đường biên cv2.RETR_EXTERNAL là lấy tất cả đường biên mà không phân cấp, CHAIN_APPOX_SIMPLE là lấy
    con, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in con:  # br = cv2.boundingRect(contours)
        x, y, w, h = cv2.boundingRect(
            c
        )  # x,y la toa độ ban đầu của đường biên, W,h là chiêu ngang và cao
        # vẽ đường vào ảnh Frame từ điểm có tọa độ x,y đến tọa độ xa nhất x+w,y+h với dường vẽ có màu là (0,255,0), độ dày là 2
        cv2.rectangle(Frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("anh", Frame)
    # max_contour = contours[0]
    # for contour in contours:
    #     if cv2.contourArea(contour) > cv2.contourArea(max_contour):
    #         max_contour = contour
    # approx = cv2.approxPolyDP(
    #     max_contour, 0.01 * cv2.arcLength(max_contour, True), True
    # )
    # x, y, w, h = cv2.boundingRect(approx)
    # cv2.rectangle(Frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # cv2.imshow("anh", Frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
