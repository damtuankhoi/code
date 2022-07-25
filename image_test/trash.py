import cv2
import numpy as np
import time

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS, 10)
fps = int(cap.get(5))
print("fps:", fps)
cap.set(3, 1280)
cap.set(4, 720)

kernel = np.ones((5, 5), np.uint8)

canvas = None

x1, y1 = 0, 0

noiseth = 800

val = 1

start_time = time.time()
x = 1
counter = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    counter += 1
    if (time.time() - start_time) > x:
        print("FPS: ", counter / (time.time() - start_time))
        counter = 0
        start_time = time.time()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_range = np.array([72, 86, 33])
    upper_range = np.array([179, 255, 255])

    mask = cv2.inRange(hsv, lower_range, upper_range)

    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours and cv2.contourArea(max(contours, key=cv2.contourArea)) > noiseth:

        c = max(contours, key=cv2.contourAqrea)

        area = cv2.contourArea(c)
        x2, y2, w, h = cv2.boundingRect(c)
        frame = cv2.rectangle(frame, (x2, y2), (x2 + w, y2 + h), (0, 0, 255), 2)
        a1 = x2
        a2 = x2 + w
        b1 = y2
        b2 = y2 + h
        print("diaginal point 1 (a1,b1) = ({},{})".format(a1, b1))
        print("diaginal point 2 (a2,b2) = ({},{})".format(a2, b2))

        def iou(box1, box2):

            xi1 = max(box1[0], box2[0])
            yi1 = max(box1[1], box2[1])
            xi2 = min(box1[2], box2[2])
            yi2 = min(box1[3], box2[3])
            inter_area = (yi2 - yi1) * (xi2 - xi1)

            box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
            box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
            union_area = box1_area + box2_area - inter_area

            # compute the IoU
            iou = inter_area / union_area

            return iou


        box2 = (a1, b1, a2, b2)
        if box2 is not None:
            box1 = box2
            print("iou = " + str(iou(box1, box2)))
        print(len(contours))
        if x1 == 0 and y1 == 0:
            x1, y1 = x2, y2
        if area > 10000:
            val = 1
            cv2.putText(frame, "blue Colour_1", (x2, y2), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255 * val))
            x1, y1 = x2, y2
        elif 8000 > area > 100:
            cv2.putText(frame, "blue Colour_2", (x2, y2), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255 * val))
            val = 0
        canvas = cv2.circle(canvas, (x2, y2), 10, [0, 0, 255 * val], -1)
    # print(x1, y1)



    frame = cv2.add(frame, canvas)

    stacked = np.hstack((canvas, frame))

    cv2.imshow('Trackbars', cv2.resize(stacked, None, fx=0.6, fy=0.6))
    cv2.imshow('mask', mask)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
