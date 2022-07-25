import cv2

# Đọc ảnh
image = cv2.imread('contour_detection.jpg')
# chuyển đổi hình ảnh sang định dạng thang độ xám
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# áp dụng ngưỡng nhị phân
ret, thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)
# visualize the binary image
cv2.imshow('Binary image', thresh)
# phát hiện các đường viền trên hình ảnh nhị phân bằng cách sử dụng cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# vẽ đường viền trên hình ảnh gốc
image_copy = image.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

# kết quả
cv2.imshow('None approximation', image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Now let's try with `cv2.CHAIN_APPROX_SIMPLE`
"""
# phát hiện các đường viền trên ảnh nhị phân bằng cách sử dụng cv2.ChAIN_APPROX_SIMPLE
contours1, hierarchy1 = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# vẽ các đường viền trên ảnh gốc bởi `CHAIN_APPROX_SIMPLE`
image_copy1 = image.copy()
cv2.drawContours(image_copy1, contours1, -1, (0, 255, 0), 2, cv2.LINE_AA)
# kết quả
cv2.imshow('Simple approximation', image_copy1)
cv2.waitKey(0)