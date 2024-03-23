import cv2
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt


def Kirsch(link_img):
    H1 = np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]])
    H2 = np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]])
    H3 = np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]])
    H4 = np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]])
    H5 = np.array([[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]])
    H6 = np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]])
    H7 = np.array([[-3, -3, -3], [5, 0, -3], [5, 5, -3]])
    H8 = np.array([[5, -3, -3], [5, 0, -3], [5, -3, -3]])
    A1 = scipy.signal.convolve(link_img, H1, mode="same", method="auto")
    A2 = scipy.signal.convolve(link_img, H2, mode="same", method="auto")
    A3 = scipy.signal.convolve(link_img, H3, mode="same", method="auto")
    A4 = scipy.signal.convolve(link_img, H4, mode="same", method="auto")
    A5 = scipy.signal.convolve(link_img, H5, mode="same", method="auto")
    A6 = scipy.signal.convolve(link_img, H6, mode="same", method="auto")
    A7 = scipy.signal.convolve(link_img, H7, mode="same", method="auto")
    A8 = scipy.signal.convolve(link_img, H8, mode="same", method="auto")
    M1 = np.maximum(A1, A2)
    M2 = np.maximum(M1, A3)
    M3 = np.maximum(M2, A4)
    M4 = np.maximum(M3, A5)
    M5 = np.maximum(M4, A6)
    M6 = np.maximum(M5, A7)
    img = np.maximum(M6, A8)
    return img


def sobel(link_img):
    Hx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    Hy = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    img = scipy.signal.convolve(
        link_img, Hx, mode="same", method="direct"
    ) + scipy.signal.convolve(link_img, Hy, mode="same", method="direct")
    return img


def robert(link_img):
    Hx = np.array([[0, 1], [-1, 0]]).astype(np.uint8)
    Hy = np.array([[-1, 0], [0, 1]]).astype(np.uint8)

    IxHx = scipy.signal.convolve(link_img, Hx, mode="same", method="direct")
    IxHy = scipy.signal.convolve(link_img, Hy, mode="same", method="direct")
    # Calculate the magnitude and direction of gradient using  Robert
    img = IxHx + IxHy
    return img


def prewitt(link_img):
    Hx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    Hy = np.array([[-1, 2, -1], [0, 0, 0], [1, 2, 1]])
    IxHx = scipy.signal.convolve(link_img, Hx, mode="same", method="direct")
    IxHy = scipy.signal.convolve(link_img, Hy, mode="same", method="direct")
    img = IxHx + IxHy
    return img


def laplace(link_img):
    H1 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    H2 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    H3 = np.array([[1, -1, 1], [-2, 5, -1], [1, -2, 1]])
    img = scipy.signal.convolve(link_img, H2, mode="same", method="direct")
    return img
