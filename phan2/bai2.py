import cv2
import numpy as np
img1 = cv2.imread('eye.jpg');
img2 = cv2.imread('eye2.jpg');
#cắt ảnh từ điểm 0,500 đến 400,500
imgcrop1 = img1[100:300, 100:400];
imgcrop2 = img2[100:300, 100:400];
#ghép 2 ảnh vào nhau
img3 = cv2.add(imgcrop1,imgcrop2);
cv2.imshow('image', img3);
cv2.waitKey(0);