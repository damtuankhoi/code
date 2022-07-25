#use trackbar
import cv2

maxScaleUp = 100
scaleFactor = 1
windowName = "Resize Image"
trackbarValue = "Scale"

# Đọc ảnh
image = cv2.imread("annotating_img.png")

# Tạo cửa sổ để hiển thị kết quả và đặt cờ thành Autosize
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

# Hàm gọi lại
def scaleImage(*args):
    # Lấy hệ số tỷ lệ từ thanh theo dõi
    scaleFactor = 1+ args[0]/100.0
    # Thay đổi kích thước hình ảnh
    scaledImage = cv2.resize(image, None, fx=scaleFactor, fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)

# Tạo thanh theo dõi và liên kết chức năng gọi lại
cv2.createTrackbar(trackbarValue, windowName, scaleFactor, maxScaleUp, scaleImage)

# Hiển thị hình ảnh
cv2.imshow(windowName, image)
c = cv2.waitKey(0)
cv2.destroyAllWindows()