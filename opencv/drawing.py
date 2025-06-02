import os, cv2

path = os.path.join('.', 'asset', 'whiteboard.jfif')

img = cv2.imread(path)

print(img.shape)

img = cv2.resize(img, (275*2, 183*2))

print(img.shape)

#line
cv2.line(img, (50, 100), (200, 300), (0, 255, 0), 3)

#rectangle
cv2.rectangle(img, (20,80), (220, 320), (0, 0, 255), 3)

#circle
cv2.circle(img, (275, 183), 100, (255, 0, 0), -1)

#text
cv2.putText(img, 'oi mama', (140, 320), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 2)

cv2.imshow('frame',img)
cv2.waitKey(0)