import os, cv2

path = os.path.join('.','asset','image.png')

image = cv2.imread(path)

print(image.shape)

cropped_image = image[0:183, 100:270]

cv2.imshow('frame',cropped_image)
cv2.waitKey(0)