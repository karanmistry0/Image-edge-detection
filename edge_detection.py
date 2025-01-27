import cv2
import os

import numpy as np

# read Image
image_path = os.path.join('.','imgs','happy.jpg')
img = cv2.imread(image_path)
img = cv2.resize(img,(747,498))

# Edge Detection
img_edge = cv2.Canny(img,90,150)
img_edge_d = cv2.dilate(img_edge,np.ones((5,5),dtype=np.uint8))
img_edge_e = cv2.erode(img_edge_d, np.ones((3,3),dtype=np.uint8))

# Visualize Image
cv2.imshow('Original Image',img)
cv2.imshow('Canny Image',img_edge)
cv2.imshow('Dilated_image',img_edge_d)
cv2.imshow('Eroded_image',img_edge_e)
cv2.waitKey(0)
cv2.destroyAllWindows()