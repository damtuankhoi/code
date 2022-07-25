import cv2
import numpy as np
im = cv2.imread('image.png')
# im = cv2.imshow('origin', im)
# Đọc ảnh
im = cv2.imread("image.png", cv2.IMREAD_GRAYSCALE)

# Thiết lập thông số SimpleBlobDetector.
params = cv2.SimpleBlobDetector_Params()
# Đổi thresholds
params.minThreshold = 10
params.maxThreshold = 200
# Lọc bởi Area.
params.filterByArea = True
params.minArea = 4
# Lọc bởi Circularity
params.filterByCircularity = True
params.minCircularity = 0.1
# Lọc bởi Convexity
params.filterByConvexity = True
params.minConvexity = 0.87

# Lọc bởi Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.1
# Tạo một máy dò với các tham số
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)
# Phát hiện đốm màu
keypoints = detector.detect(im)
# Vẽ các đốm màu với những vòng tròn màu đỏ
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS đảm bảo
# kích thước của vòng tròn tương ứng với kích thước của đốm màu
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)