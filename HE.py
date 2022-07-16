# -*- coding: utf-8 -*-
import os

import cv2


def HE(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    channels = cv2.split(hsv)
    cv2.equalizeHist(channels[2], channels[2])
    cv2.merge(channels, hsv)
    cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB, img)
    return img


data_path = r''
img_list = os.listdir(data_path)
img = cv2.imread(os.path.join(data_path))
img_he = HE(img)
cv2.imshow('CLAHE', he)
cv2.waitKey()
