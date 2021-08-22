# -*- coding: utf-8 -*-
"""Object detection using cvlib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://drive.google.com/drive/folders/18AddcDuF2KZ7maszFqsJOr7Rz1Hlvr2E
"""

#pip install cvlib

#!pip install opencv-contrib-python==3.4.13.47 --force-reinstall

import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly

from google.colab import files
uploaded = files.upload()

from IPython.display import Image
Image('cars.jpeg')

image = cv2.imread('cars.jpeg')
box,label,count = cv.detect_common_objects(image)
output = draw_bbox(image,box,label,count)
plt.imshow(output)
plt.show()
print("Number of cars in this image are: ",str(label.count('car')))

