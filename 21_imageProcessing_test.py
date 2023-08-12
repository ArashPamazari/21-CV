# pip install opencv-python
# famous library of image processing cv means computer vision
# import cv2

import cv2

image = cv2.imread('s.JPG',0)   #imread = image read / Open image with cv / 0 = open image in gray

print(image)                    # show araye image in termianl

#----------------------------------------#

image[0,0] = 255               #satre 0 , soton 0 om ro 255 bokon / 255 = sefid kamel , 0 = siah kamel
image[0,1] = 255
image[1,0] = 255
image[1,1] = 255
#----------------------------------------#
image[0:5 , 0:12] = 255         # az satre 0 om ta 5 om va az soton 0 om ta 12 hamaro 255 kon
#----------------------------------------#
image[0:960 , 0:40] = 0         # ye ghab kenar tasvir
#----------------------------------------#

print(image.shape)              # andaze tasvir bedonim cheqadre , chandta satr dare , chandta soton
cv2.imwrite('result.jpg',image) #in image ro baram ba esme result save kon

cv2.imshow('mohemnist',image)   #in def image ro be sorat tasvir neshon mide / parameter aval mohem nist (onvan panjere ie ke baz mishe)
cv2.waitKey()                   #baray inke tasvir baste nashe

#------------------------------_----------------------------#

# jabejaee ghesmati az tasvir
face = image[600:250 , 200:350]

print(face.shape)              #Size face cheqadre
image[400:590,50:200]= face
cv2.imshow('output',image)
cv2.waitKey()

#-------------------------------------#
# taqire Size va abAd
image = cv2.imread('s.JPG',0)
new_image = cv2.resize(image,(320,480))
cv2.imshow('output',new_image)
cv2.waitKey()

#------------------------------_----------------------------#

import cv2

image = cv2.imread('s.JPG',0)

threshold = 100                   # 100 meghdar threshold ( Astane ya hamon marz ) amone
height ,width = image.shape

# agar bekhaym sefia sefidtar va siaha siahtar beshe :
for i in range(height):
  for j in range(width):
    if image[i,j] > threshold:
      image[i,j] = 255
    elif image[i,j] <= threshold:
      image[i,j]= 0

# agar bekhaym jaye sefida ba siaha avaz beshe :   negative filter
for i in range(height):
  for j in range(width):
    image[i,j] = 255-image[i,j]      # math Rule


cv2.imwrite('result.jpg',image)
cv2.imshow('output',image)
cv2.waitKey()