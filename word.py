import numpy as np
import cv2


width = 200
height = 200


img = np.ones((height, width), dtype=np.uint8) * 255


thickness = 6
point1 = (40, 160)
point2 = (100, 40)
point3 = (160, 160)


cv2.line(img, point1, point2, 0, thickness)
cv2.line(img, point2, point3, 0, thickness)


horizontal_line = (80, 120)
cv2.line(img, (point1[0], horizontal_line[1]), (point3[0], horizontal_line[1]), 0, thickness)


cv2.imwrite('Character A.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
