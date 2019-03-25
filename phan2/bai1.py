import cv2
#thư viện xử lý tính toán
import numpy as np
img = cv2.imread('opencv.jpg');
#cắt ảnh từ điểm 0,500 đến 400,500
imgcrop = img[0:500, 400:500];
cv2.imshow('image', imgcrop);
cv2.waitKey(0);
cv2.destroyAllWindows();