import cv2
import numpy as np
import pandas as pd
import sklearn.cluster
from matplotlib import pyplot as plt

gray = cv2.imread(
    r"C:\Users\mtcle\OneDrive\WorkSpace\computer-vision\data\external\image\moon.png", 0
)
print(gray)

# km = sklearn.cluster.k_means(gray, n_clusters=3)
# plt.figure()
# plt.subplot(121), plt.imshow(cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR))
# plt.title("Original"), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(km.labels_.reshape(gray.shape[:-1]))
# plt.title("K-Means Clustering"), plt.xticks([]), plt.yticks([])
# plt.show()

T0 = np.min(gray)
Tk = np.max(gray)
k = 2
Tp = np.zeros(k + 1)
Tc = np.zeros(k + 1)
for i in range(k + 1):
    if i == 0:
        Tp[i] = T0
    elif i == k:
        Tp[i] = Tk
    else:
        value = i * ((Tk - T0) / k) + T0
        Tp[i] = value

c = []
# print(Tp[i])
heigh, wight = gray.shape
status = 0
while status != k:
    # print(heigh,wight)
    count = np.zeros(k)
    # thêm các ma trận có kich thước bằng ảnh với giá trị bằng 0 vào 1 list
    for i in range(k):
        c.append(np.zeros((heigh, wight)))
    for h in range(heigh):
        for w in range(wight):
            for i in range(k):
                if Tp[i] <= gray[h][w] <= Tp[i + 1]:
                    (c[i])[h][w] = gray[h][
                        w
                    ]  # add giá trị điểm ảnh vào đúng tạo độ đó trên vùng
                    count[i] = count[i] + 1  # tăng số lần đếm cho phần tử đã chứa điểm

    m = np.zeros(k)
    for i in range(k):
        m[i] = np.sum(c[i]) / count[i]

    # i chạy từ 0 đến 5 vì có 6 ngưỡng
    for i in range(k + 1):
        if i == 0:
            Tc[i] = T0
        elif i == k:
            Tc[i] = Tk
        else:
            Tc[i] = (m[i - 1] + m[i]) / 2
    for i in range(k + 1):
        condition = np.abs(Tc[i] - Tp[i])
        if 0 <= condition <= 1:
            Tp[i] = Tc[i]
            status = status + 1
        else:
            Tp[i] = Tc[i]
    print(f"previous{Tp}")
    print(f"Current{Tc}")

img = c[k - 1].astype(np.uint8)
cv2.imshow("bal", img)
cv2.waitKey()
