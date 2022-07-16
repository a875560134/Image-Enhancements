# -*- coding: utf-8 -*-

import cv2
import numpy as np


def singleScaleRetinexTemp(img, sigma):
    # 按照公式计算
    _temp = cv2.GaussianBlur(img, (0, 0), sigma)
    gaussian = np.where(_temp == 0, 0.001, _temp)
    retinex = np.log10(img + 0.01) - np.log10(gaussian)

    return retinex


def multiScaleRetinex(img, sigma_list):
    retinex = np.zeros_like(img * 1.0)
    for sigma in sigma_list:
        print("sigma:", sigma)
        retinex += singleScaleRetinexTemp(img, sigma)
    img_msr = retinex / len(sigma_list)
    for i in range(img_msr.shape[2]):
        img_msr[:, :, i] = (img_msr[:, :, i] - np.min(img_msr[:, :, i])) / (
                    np.max(img_msr[:, :, i]) - np.min(img_msr[:, :, i])) * 255
    img_msr = np.uint8(np.minimum(np.maximum(img_msr, 0), 255))
    return img_msr


data_path = r'C:\Users\sc\Desktop\1.jpeg'
img = cv2.imread(data_path)
img_multiScaleRetinex = multiScaleRetinex(img + 1.0, [15, 80, 250])
cv2.imshow('CLAHE', img_multiScaleRetinex)
cv2.waitKey()
