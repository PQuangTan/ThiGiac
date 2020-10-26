import numpy as np
import cv2
img_girl = cv2.imread("girl.jpg", 1)
img = cv2.imread ("fire.jpg",1);
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
imga = cv2.imread ("mask.png",0);

img3 = cv2.bitwise_and(img, img, mask=imga)
img3 = cv2.cvtColor(img3, cv2.COLOR_HSV2BGR)
img3= cv2.add(img3,img_girl)

cv2.imshow("anh ghep", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()