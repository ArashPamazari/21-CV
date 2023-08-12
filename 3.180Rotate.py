import cv2

image_three = cv2.imread('3.jpg', 0)

rotate_image = image_three[::-1, ::-1]  #tamame satrha ro maAkos va sotonha MaAkos 

cv2.imwrite('Rotate_image.jpg', rotate_image)

cv2.waitKey()