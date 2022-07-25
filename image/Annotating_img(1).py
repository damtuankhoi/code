#use mouse
import cv2

# Danh sách để lưu trữ tọa độ hộp giới hạn
top_left_corner=[]
bottom_right_corner=[]

# hàm sẽ được gọi khi nhập chuột
def drawRectangle(action, x, y, flags, *userdata):
  # Tham chiếu các biến toàn cục
  global top_left_corner, bottom_right_corner
  # Đánh dấu góc trên cùng bên trái khi nhấn nút chuột trái
  if action == cv2.EVENT_LBUTTONDOWN:
    top_left_corner = [(x,y)]
  # Khi thả nút chuột trái, đánh dấu góc dưới cùng bên phải
  elif action == cv2.EVENT_LBUTTONUP:
    bottom_right_corner = [(x,y)]
    # Vẽ hình chữ nhật
    cv2.rectangle(image, top_left_corner[0], bottom_right_corner[0], (0,255,0),2, 8)
    cv2.imshow("Window",image)

# Đọc ảnh
image = cv2.imread("annotating_img.png")
# Tạo một hình ảnh tạm thời, sẽ hữu ích để xóa bản vẽ
temp = image.copy()
# Tạo một cửa sổ được đặt tên
cv2.namedWindow("Window")
# hàm highgui được gọi khi sự kiện chuột xảy ra
cv2.setMouseCallback("Window", drawRectangle)

k=0
# Đóng cửa sổ khi phím q được nhấn
while k!=113:
  # Hiển thị ảnh
  cv2.imshow("Window", image)
  k = cv2.waitKey(0)
  # Nếu nhấn c, hãy xóa cửa sổ bằng hình ảnh giả
  if (k == 99):
    image= temp.copy()
    cv2.imshow("Window", image)

cv2.destroyAllWindows()