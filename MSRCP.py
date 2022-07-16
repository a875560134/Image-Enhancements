# -*- coding: utf-8 -*-
import math
import os

import cv2
import numpy as np


def MSRCP(img, sigma_list, low_clip, high_clip):
    img = np.float64(img) + 1.0
    intensity = np.sum(img, axis=2) / img.shape[2]
    retinex = multiScaleRetinex(intensity, sigma_list)
    intensity = np.expand_dims(intensity, 2)
    retinex = np.expand_dims(retinex, 2)
    intensity1 = simplestColorBalance(retinex, low_clip, high_clip)
    intensity1 = (intensity1 - np.min(intensity1)) / \
                 (np.max(intensity1) - np.min(intensity1)) * \
                 255.0 + 1.0
    img_msrcp = np.zeros_like(img)
    for y in range(img_msrcp.shape[0]):
        for x in range(img_msrcp.shape[1]):
            B = np.max(img[y, x])
            A = np.minimum(256.0 / B, intensity1[y, x, 0] / intensity[y, x, 0])
            img_msrcp[y, x, 0] = A * img[y, x, 0]
            img_msrcp[y, x, 1] = A * img[y, x, 1]
            img_msrcp[y, x, 2] = A * img[y, x, 2]
    img_msrcp = np.uint8(img_msrcp - 1.0)
    return img_msrcp


data_path = r''
img = cv2.imread(data_path)
img_msrcp = MSRCP(
    img,
    [15, 80, 250],
    0.01,
    0.99
)
cv2.imshow('MSRCP', img_msrcp)
cv2.waitKey()
