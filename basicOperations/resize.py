import os
import cv2

path = os.path.join('.','asset','image.png')

image = cv2.imread(path)

resized_image = cv2.resize(image,(550, 366))

print(resized_image.shape)

cv2.imshow('frame1', image)
cv2.imshow('frame2', resized_image)

cv2.waitKey(0)