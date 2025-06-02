import os, cv2
import numpy as np

img = cv2.imread(os.path.join('.','asset','player.jpg'))

img_edge = cv2.Canny(img, 200, 300)

img_edge_d = cv2.dilate(img_edge, np.ones((5, 5), dtype=np.int8))
img_edge_e = cv2.erode(img_edge_d, np.ones((5, 5), dtype=np.int8))

cv2.imshow('player', img_edge_d)
cv2.imshow('player2', img_edge_e)
cv2.waitKey(0)