import cv2

image_one = cv2.imread('1.jpg', 0)
image_two = cv2.imread('2.jpg', 0)

image_one[:,:] = 255 - image_one[:,:] #switch color
image_two[:,:] = 255 - image_two[:,:] #entekhab tamame andis ha va kam kardan az 255

cv2.imwrite('Output1.jpg', image_one)
cv2.imwrite('output2.jpg', image_two)

cv2.waitKey()