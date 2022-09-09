from imutils import paths
import cv2
import os
import numpy as np

for path in paths.list_images('mask'):
    img = cv2.imread(path)
    ori = img.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    sensitivity = 100
    lower_white = np.array([0,0,255-sensitivity])
    upper_white = np.array([255,sensitivity,255])

    mask = cv2.inRange(img, lower_white, upper_white)

    cv2.imwrite('new_mask/{}'.format(path.split('/')[-1]), mask)