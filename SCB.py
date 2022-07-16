# -*- coding: utf-8 -*-
import cv2
import numpy as np


def simplestColorBalance(img, low_clip=0.001, high_clip=0.999):
    total = img.shape[0] * img.shape[1]
    for i in range(img.shape[2]):
        unique, counts = np.unique(img[:, :, i], return_counts=True)
        current = 0
        for u, c in zip(unique, counts):
            if float(current) / total < low_clip:
                low_val = u
            if float(current) / total < high_clip:
                high_val = u
            current += c

        img[:, :, i] = np.maximum(np.minimum(img[:, :, i], high_val), low_val)

    return img


data_path = r'C:\Users\sc\Desktop\1.jpeg'
img = cv2.imread(data_path)
img_clahe = simplestColorBalance(img)
cv2.imshow('img_clahe', img_clahe)
cv2.waitKey()
