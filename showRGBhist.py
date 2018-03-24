import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('3.JPG')
color = ('r', 'g', 'b')
for i, col in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim(0, 256)
    plt.show()