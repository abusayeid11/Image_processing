import os, cv2
path = os.path.join('.','asset','image.png')

img = cv2.imread(path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('frame',img_gray)
cv2.imshow('frame2', img_rgb)
cv2.imshow('frame3', img_hsv)
cv2.waitKey(0)