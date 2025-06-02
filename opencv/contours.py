import os, cv2

path = os.path.join('.', 'asset', 'birds.jpg')

img = cv2.imread(path)

print(img.shape)

img = cv2.resize(img, (800, 600))



cv2.imshow('frame', img)

cv2.waitKey(0)