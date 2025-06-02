import os, cv2

path = os.path.join('.', 'asset', 'bear.jfif')

img = cv2.imread(path)
print(img.shape)
resized_img = cv2.resize(img, (275*2, 183*2))


img_gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(resized_img, cv2.COLOR_RGB2GRAY)

thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 20)

thresh = cv2.blur(thresh,(10, 10))

cv2.imshow('bear',img_gray)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)