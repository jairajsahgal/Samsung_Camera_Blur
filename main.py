import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
import numpy as np

imgList = []
cap = cv2.VideoCapture(0)
segmentor = SelfiSegmentation(model=0)
fpsReader = cvzone.FPS()
indexImg = 0
blurIndex = 0
a = [(0, 0)]
for i in range(1, 100, 1):
    a.append((2 * i, 2 * i))
while True:
    success, img = cap.read()
    if blurIndex != 0:
        bg_image = cv2.blur(src=img, ksize=a[blurIndex])
    else:
        bg_image = img
    imgList.append(bg_image)
    imgOut = segmentor.removeBG(img, imgList[indexImg], threshold=0.5)
    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
    cv2.imshow("Image", imgStacked)
    key = cv2.waitKey(1)
    if key == ord('a'):
        if indexImg > 0:
            indexImg -= 1
    elif key == ord('d'):
        if indexImg < len(imgList) - 1:
            indexImg += 1
    elif key == ord('q'):
        break
    elif key == ord('z'):
        if blurIndex > 0:
            blurIndex -= 1
    elif key == ord('c'):
        if blurIndex < len(a) - 1:
            blurIndex += 1
    imgList.pop()
