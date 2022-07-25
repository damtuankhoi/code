import cv2
import numpy as np

# đọc tên lớp ImageNet
with open('classification_classes_ILSVRC2012.txt', 'r') as f:
    image_net_names = f.read().split('\n')
# tên lớp cuối cùng (chỉ là từ đầu tiên của nhiều tên ImageNet cho một hình ảnh)
class_names = [name.split(',')[0] for name in image_net_names]

# tải mô hình mạng nơron
model = cv2.dnn.readNet(model='DenseNet_121.caffemodel', config='DenseNet_121.prototxt', framework='Caffe')

# tải hình ảnh từ đĩa
image = cv2.imread('image_1.jpg')
# tạo đốm màu từ hình ảnh
blob = cv2.dnn.blobFromImage(image=image, scalefactor=0.01, size=(224, 224), mean=(104, 117, 123))
# đặt đốm màu đầu vào cho mạng nơ-ron
model.setInput(blob)
# chuyển tiếp blog hình ảnh thông qua mô hình
outputs = model.forward()

final_outputs = outputs[0]
# tạo tất cả các đầu ra 1D
final_outputs = final_outputs.reshape(1000, 1)
# lấy nhãn lớp
label_id = np.argmax(final_outputs)
# chuyển đổi điểm đầu ra thành xác suất softmax
probs = np.exp(final_outputs) / np.sum(np.exp(final_outputs))
# nhận được xác suất cao nhất cuối cùng
final_prob = np.max(probs) * 100.
# ánh xạ độ tin cậy tối đa cho các tên nhãn lớp
out_name = class_names[label_id]
out_text = f"{out_name}, {final_prob:.3f}"

# đặt văn bản tên lớp lên đầu hình ảnh
cv2.putText(image, out_text, (25, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow('Image', image)
cv2.waitKey(0)