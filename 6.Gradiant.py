import cv2
import numpy as np


image_size = 800

# ایجاد تصویر مربعی سفید
image = np.ones((image_size, image_size, 3), dtype=np.uint8) * 255

# تغییر رنگ سطر به سطر از بالا به سمت مشکی
for row in range(image_size):
    intensity = int(row / image_size * 255)  # محاسبه مقدار شدت رنگ مشکی بر اساس سطر
    image[row, :, :] = (intensity, intensity, intensity)

for row in range(image_size):
    intensity = int((image_size - row) / image_size * 255)  # محاسبه مقدار شدت رنگ سفید بر اساس سطر
    image[row, :, :] = (intensity, intensity, intensity)

# نمایش تصویر
cv2.imwrite('result.jpg',image)

cv2.destroyAllWindows()
