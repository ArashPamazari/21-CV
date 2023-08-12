import cv2
import numpy as np


image_size = 800


image = np.ones((image_size, image_size, 3), dtype=np.uint8) * 255


for row in range(image_size):
    intensity = int(row / image_size * 255) 
    image[row, :, :] = (intensity, intensity, intensity)

for row in range(image_size):
    intensity = int((image_size - row) / image_size * 255)  
    image[row, :, :] = (intensity, intensity, intensity)

cv2.imwrite('result.jpg',image)


