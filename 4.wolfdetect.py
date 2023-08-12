import cv2

image = cv2.imread('4.jpg', 0)

height, width = image.shape
threshold = 160

for i in range(height):
  for j in range(width):
    if image[i,j] > threshold:
      image[i,j] = 255
    elif image[i,j] <= threshold:
      image[i,j]= 0

cv2.imwrite('Wolf.jpg', image)

cv2.waitKey()