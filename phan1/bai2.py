#import thư viện
import cv2
#đọc ảnh
img = cv2.imread('opencv.jpg');
#vẽ một đường kẻ từ tọa độ x, y (0,0) đến (500,100) với màu (RED,GREEB,BLUE) độ dày đường line là 8px
cv2.line(img, (0,0), (500,100), (255,255,0), 8);
cv2.imwrite('anhmoi.jpg', img);
cv2.destroyAllWindows();