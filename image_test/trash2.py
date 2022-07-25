import cv2
from matplotlib.transforms import Bbox
import numpy as np
import time

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS, 10)
fps = int(cap.get(5))
# print("fps:", fps)
cap.set(3, 1280)
cap.set(4, 720)

kernel = np.ones((5, 5), np.uint8)

start_time = time.time()
p = 1
counter = 0

IDS = []
def iou(box1, box2):
                xi1 = max(box1[0], box2[0])
                yi1 = max(box1[1], box2[1])
                xi2 = min(box1[2], box2[2])
                yi2 = min(box1[3], box2[3])
                inter_area = (yi2 - yi1) * (xi2 - xi1)

                box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
                box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
                union_area = box1_area + box2_area - inter_area

                iou = inter_area / (union_area + 0.00000000000000000001)

                return iou
flag_initial = True
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    if ret:
        counter += 1
        canidate_0 = None
        canidate_1 = None
        canidate_2 = None

        
        if (time.time() - start_time) > p:
            # print("FPS: ", counter / (time.time() - start_time))
            counter = 0
            start_time = time.time()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # lower_range = np.array([72, 86, 33])
        # upper_range = np.array([179, 255, 255])
        lower_range = np.array([96, 149, 49])
        upper_range = np.array([147, 255, 255])

        mask = cv2.inRange(hsv, lower_range, upper_range)

        mask = cv2.erode(mask, kernel, iterations=1)
        mask = cv2.dilate(mask, kernel, iterations=2)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        area = [cv2.contourArea(contour) for contour in contours]
        box_new = []
        for pic, contour in enumerate(contours):
            x, y, w, h = cv2.boundingRect(contour)
            area_1 = cv2.contourArea(contour)
            a1 = x
            a2 = x + w
            b1 = y
            b2 = y + h
            if area_1 > 500:
                box_new.append([a1, b1, a2, b2 ])
        if len(IDS) > 0:
            for i in range(len(IDS)):
                tmp = []
            
                for j in range(len(box_new)):
                    iou_new = iou(IDS[i], box_new[j])
                    if 0 < iou_new < 1 :
                        tmp.append([iou_new,box_new[j]])
                print('tmp:', tmp)
                max_v = 0
                for k in range(len(tmp)):
                    if tmp[k][0] > max_v:
                        canidate = tmp[k][1]
                        max_v = tmp[k][0]
                print(canidate,i)
                if i == 0:
                    canidate_0 = canidate
                if i == 1:
                    canidate_1 = canidate
                if i == 2:
                    canidate_2 = canidate
                    
            print(canidate_0, max_v)
        IDS = box_new
        print('IDS:', IDS)
    if canidate_0 is not None:
        cv2.rectangle(frame, (canidate_0[0], canidate_0[1]), (canidate_0[2], canidate_0[3]), (0, 0, 255), 2)
        # for i in range(len(box_new)):
        #     cv2.rectangle(frame, (box_new[i][0],box_new[i][1]), (box_new[i][2], box_new[i][3]), (250, 0, 255), 2)
        cv2.putText(frame, "0", (canidate_0[0], canidate_0[1]), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
    if canidate_1 is not None:
        cv2.rectangle(frame, (canidate_1[0], canidate_1[1]), (canidate_1[2], canidate_1[3]), (0, 0, 255), 2)
        # for i in range(len(box_new)):
        #     cv2.rectangle(frame, (box_new[i][0],box_new[i][1]), (box_new[i][2], box_new[i][3]), (250, 0, 255), 2)
        cv2.putText(frame, "1", (canidate_1[0], canidate_1[1]), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
    if canidate_2 is not None:
        cv2.rectangle(frame, (canidate_2[0], canidate_2[1]), (canidate_2[2], canidate_2[3]), (0, 0, 255), 2)
        # for i in range(len(box_new)):
        #     cv2.rectangle(frame, (box_new[i][0],box_new[i][1]), (box_new[i][2], box_new[i][3]), (250, 0, 255), 2)
        cv2.putText(frame, "2", (canidate_2[0], canidate_2[1]), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break 

cap.release()
cv2.destroyAllWindows()