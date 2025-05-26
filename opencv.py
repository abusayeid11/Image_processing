import os, cv2

path = os.path.join('.','asset','image.png')

image = cv2.imread(path)

cv2.imwrite(os.path.join('.','asset','image_out.png'), image)

cv2.imshow('frame', image)
cv2.waitKey(0)