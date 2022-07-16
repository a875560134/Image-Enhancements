# -*- coding: utf-8 -*-
import math
import os
import cv2
import numpy as np


def singleScaleRetinex(img, sigma):

    _temp = cv2.GaussianBlur(img, (0, 0), sigma)
    gaussian = np.where(_temp == 0, 0.001, _temp)
    img_ssr = np.log10(img + 0.01) - np.log10(gaussian)

    for i in range(img_ssr.shape[2]):
        img_ssr[:, :, i] = (img_ssr[:, :, i] - np.min(img_ssr[:, :, i])) / \
                           (np.max(img_ssr[:, :, i]) - np.min(img_ssr[:, :, i])) * 255
    img_ssr = np.uint8(np.minimum(np.maximum(img_ssr, 0), 255))
    return img_ssr


data_path = r'C:/Users/sc/Desktop/1.jpeg'
img = cv2.imread(data_path)
img_SSR = singleScaleRetinex(img+1.0,300)
cv2.imshow('img_SSR', img_SSR)
cv2.waitKey()
