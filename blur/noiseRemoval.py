import cv2, os

path = os.path.join('.', 'asset', 'noisyImage.png')

img = cv2.imread(path)

k = 7

#img_blur = cv2.blur(img, (k,k))

#img_gaussian_blur = cv2.GaussianBlur(img, (k, k), 3)

img_median_blur = cv2.medianBlur(img, k)

cv2.imshow('image',img)
cv2.imshow('blur',img_median_blur)

cv2.waitKey(0)