import cv2
import time
import numpy as np

# load the COCO class names
with open('object_detection_classes_coco.txt', 'r') as f:
    class_names = f.read().split('\n')

# lấy một mảng màu khác nhau cho mỗi lớp
COLORS = np.random.uniform(0, 255, size=(len(class_names), 3))

# load the DNN model
model = cv2.dnn.readNet(model='frozen_inference_graph.pb', config='ssd_mobilenet_v2_coco_2018_03_29.pbtxt.txt', framework='TensorFlow')

# capture the video
cap = cv2.VideoCapture('video_1.mp4')
# lấy chiều rộng và chiều cao của khung video để lưu video thích hợp
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
# create the `VideoWriter()` object
# out = cv2.VideoWriter('video_result.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

# phát hiện các đối tượng trong mỗi khung hình của video
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        image = frame
        image_height, image_width, _ = image.shape
        # create blob from image
        blob = cv2.dnn.blobFromImage(image=image, size=(300, 300), mean=(104, 117, 123), swapRB=True)
        # bắt đầu thời gian tính toán FPS
        start = time.time()
        model.setInput(blob)
        output = model.forward()
        # kết thúc thời gian sau khi phát hiện
        end = time.time()
        # tính toán FPS để phát hiện khung hình hiện tại
        fps = 1 / (end - start)
        # vòng lặp qua từng phát hiện
        for detection in output[0, 0, :, :]:
            # trích xuất độ tin cậy của phát hiện
            confidence = detection[2]
            # vẽ các hộp giới hạn chỉ khi độ tin cậy phát hiện ở trên
            # một ngưỡng nhất định, nếu không, hãy bỏ qua
            if confidence > .4:
                # get the class id
                class_id = detection[1]
                # map the class id to the class
                class_name = class_names[int(class_id) - 1]
                color = COLORS[int(class_id)]
                # lấy tọa độ hộp giới hạn
                box_x = detection[3] * image_width
                box_y = detection[4] * image_height
                # Lấy chiều cao và chiều sâu cho hộp giới hạn
                box_width = detection[5] * image_width
                box_height = detection[6] * image_height
                # vẽ một hình chữ nhật xung quanh mỗi đối tượng được phát hiện
                cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), color, thickness=2)
                # đặt văn bản tên lớp vào đối tượng được phát hiện
                cv2.putText(image, class_name, (int(box_x), int(box_y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                # đặt văn bản FPS lên đầu khung
                cv2.putText(image, f"{fps:.2f} FPS", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('image', image)
        # out.write(image)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()