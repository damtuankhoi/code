import cv2
import numpy as np

# tải tên lớp COCO
with open('object_detection_classes_coco.txt', 'r') as f:
    class_names = f.read().split('\n')

# lấy một mảng màu khác nhau cho mỗi lớp
COLORS = np.random.uniform(0, 255, size=(len(class_names), 3))

# tải mô hình DNN
model = cv2.dnn.readNet(model='frozen_inference_graph.pb', config='ssd_mobilenet_v2_coco_2018_03_29.pbtxt.txt', framework='TensorFlow')

# Đọc ảnh
image = cv2.imread('image_2.jpg')
image_height, image_width, _ = image.shape
# Tạo đốm màu từ ảnh
blob = cv2.dnn.blobFromImage(image=image, size=(300, 300), mean=(104, 117, 123), swapRB=True)
# Tạo đốm màu từ ảnh
model.setInput(blob)
# chuyển tiếp qua mô hình để thực hiện phát hiện
output = model.forward()

# vòng lặp qua mỗi phát hiện
for detection in output[0, 0, :, :]:
    # trích xuất độ tin cậy của phát hiện
    confidence = detection[2]
    # vẽ các hộp giới hạn chỉ khi độ tin cậy phát hiện ở trên
    # một ngưỡng nhất định, nếu không, hãy bỏ qua
    if confidence > .4:
        # lấy class id
        class_id = detection[1]
        # map the class id to the class
        class_name = class_names[int(class_id)-1]
        color = COLORS[int(class_id)]
        # lấy tọa độ hộp giới hạn
        box_x = detection[3] * image_width
        box_y = detection[4] * image_height
        # lấy chiều rộng và chiều cao của hộp giới hạn
        box_width = detection[5] * image_width
        box_height = detection[6] * image_height
        # vẽ một hình chữ nhật xung quanh mỗi đối tượng được phát hiện
        cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), color, thickness=2)
        # đặt văn bản FPS lên đầu khung
        cv2.putText(image, class_name, (int(box_x), int(box_y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

cv2.imshow('image', image)
cv2.waitKey(0)