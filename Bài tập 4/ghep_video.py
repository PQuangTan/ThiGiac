import numpy as np
import cv2

cap = cv2.VideoCapture('fire.mp4')
dim = (367, 550)
img_girl = cv2.imread("girl.jpg", 1)
mask = cv2.imread ("mask.png",0);
while(cap.isOpened()):
    ret, frame = cap.read()

    # frame = frame[1000:1550, 1000:1367]
    frame = cv2.resize(frame, dim)
    # print("size", frame.shape)

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    img_add_mask = cv2.bitwise_and(img, img, mask=mask)
    img_add_mask = cv2.cvtColor(img_add_mask, cv2.COLOR_HSV2BGR)
    img3= cv2.add(img_add_mask,img_girl)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',img3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()