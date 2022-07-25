import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(1)
index_count = 0
while True:
    _, frame = cap.read()
    frame = cv2.GaussianBlur(frame, (5, 5), cv2.BORDER_DEFAULT)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blue_lower= np.array([72, 86, 33])
    blue_upper = np.array([179, 255, 255])
    # blue_lower= np.array([0, 160, 0])
    # blue_upper = np.array([10,190,255])
    red_mask = cv2.inRange(hsv, blue_lower, blue_upper)
    # kernal = np.ones((5, 5), "uint8")

    mask = cv2.inRange(hsv, blue_lower, blue_upper)
    dst = cv2.GaussianBlur(frame, (5, 5), cv2.BORDER_DEFAULT)
    red_mask = cv2.dilate(red_mask, (5,5))
    res_red = cv2.bitwise_and(frame, frame, mask=red_mask)
    res = cv2.bitwise_and(frame, dst, mask = mask)
    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            x, y, w, h = cv2.boundingRect(contour)
            roi = frame[y:y + h, x:x + w]
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            print(frame)
        print(area)
        if (area > 1500):
            cv2.putText(frame, "Red Colour_1", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
        elif area > 100 and area < 1400:
            cv2.putText(frame, "Red Colour_2", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
            try:
                cv2.imshow('crop', roi)
                # index_count += 1
                # cv2.imwrite('C:/Users/Administrator/PycharmProjects/image_test/crop_roi/' + str(index_count) + '.png', roi)
            except:
                print('error')
                pass
    cv2.imshow("Gaussian Smoothing", np.hstack((frame, dst)))
    # cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    plt.imshow(hsv)
    plt.show()
    cv2.imshow('res', res)
    k = cv2.waitKey(5)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
