import cv2
import numpy as np
img = cv2.imread('eye.jpg');
print('chieu rong');
print(img.shape[0]);
print('chieu cao');
print(img.shape[1]);
#resize ảnh
img_resize = cv2.resize(src=img, dsize=(300, 300));
new_img = 'eye_new.jpg';
cv2.imwrite(new_img, img_resize);
