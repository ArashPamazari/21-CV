import cv2

img = cv2.imread('me.jpg', 0)

height, width = img.shape

# ijad line meshki
for i in range(height):
  for j in range(width):
    if 70 < i+j < 100:
      img[i, j] = 0

cv2.imwrite('metarhim.jpg', img)

cv2.waitKey()