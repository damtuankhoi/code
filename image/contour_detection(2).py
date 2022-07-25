import cv2

# Đọc ảnh
image = cv2.imread('contour_detection.png')

# tách kênh B, G, R
blue, green, red = cv2.split(image)

# phát hiện đường viền bằng cách sử dụng kênh màu xanh lam và không có ngưỡng
contours1, hierarchy1 = cv2.findContours(image=blue, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# vẽ đường viền trên ảnh gốc
image_contour_blue = image.copy()
cv2.drawContours(image=image_contour_blue, contours=contours1, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
# kết quả
cv2.imshow('Contour detection using blue channels only', image_contour_blue)

# phát hiện đường viền bằng cách sử dụng kênh màu xanh lá và không có ngưỡng
contours2, hierarchy2 = cv2.findContours(image=green, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
# vẽ đường viền trên ảnh gốc
image_contour_green = image.copy()
cv2.drawContours(image=image_contour_green, contours=contours2, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
# kết quả
cv2.imshow('Contour detection using green channels only', image_contour_green)

# phát hiện đường viền bằng cách sử dụng kênh màu đỏ và không có ngưỡng
contours3, hierarchy3 = cv2.findContours(image=red, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
# vẽ đường viền trên ảnh gốc
image_contour_red = image.copy()
cv2.drawContours(image=image_contour_red, contours=contours3, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
# kết quả
cv2.imshow('Contour detection using red channels only', image_contour_red)
cv2.waitKey(0)