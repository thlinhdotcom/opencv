#import thư viện
import cv2
#đọc ảnh
img = cv2.imread('opencv.jpg');
#hiển thị ảnh lên
cv2.imshow('image', img);
#bấm 1 phím bất kỳ để tắt của sổ
cv2.waitKey(0);
#giải phòng bộ nhớ
cv2.destroyAllWindows();