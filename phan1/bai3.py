import cv2
img = cv2.imread('opencv.jpg');
#lấy chiều rộng, chiều cao của bức ảnh
print('chieu rong');
print(img.shape[0]);
print('chieu cao');
print(img.shape[1]);
#lấy kích thước ảnh
print('kich thuoc tinh theo byte');
print(img.size);
