import os, cv2

path = os.path.join('.', 'asset', 'click.jfif')

img = cv2.imread(path)

k = 7

img_blur = cv2.blur(img, (k, k))
img_gaussian_blur = cv2.GaussianBlur(img, (k,k), 3)
img_median_blur = cv2.medianBlur(img, k)

cv2.imshow('img', img)
cv2.imshow('blur', img_blur)
cv2.imshow('gaussian_blur', img_gaussian_blur)
cv2.imshow('median_blur', img_median_blur)

cv2.waitKey(0)