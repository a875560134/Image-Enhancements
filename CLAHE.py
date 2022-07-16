# -*- coding: utf-8 -*-
import os

import cv2


def CLAHE(image):
    b, g, r = cv2.split(image)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    b = clahe.apply(b)
    g = clahe.apply(g)
    r = clahe.apply(r)
    image = cv2.merge([b, g, r])
    return image


data_path = r''
img_list = os.listdir(data_path)
img = cv2.imread(os.path.join(data_path))
img_clahe = CLAHE(img)
cv2.imshow('CLAHE', img_clahe)
cv2.waitKey()
