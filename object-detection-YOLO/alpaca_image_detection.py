from ultralytics import YOLO
from PIL import Image

import cv2

import os

def convert_jfif_to_jpg(path):
    img = Image.open(path)
    new_path = path.replace('.jfif', '.jpg')
    img.save(new_path,'JPEG')
    return new_path

path = 'C:/Users/UAE LAPTOP BAZAR/Documents/DevyJonesLocker/python-image/Image_processing/object-detection-YOLO/colab_runs/detect/train/weights/best.pt'
model = YOLO(path)

img_path = convert_jfif_to_jpg('C:/Users/UAE LAPTOP BAZAR/Documents/DevyJonesLocker/python-image/Image_processing/object-detection-YOLO/content/alpaca1.jfif')
results = model.predict(img_path)

img = results[0].plot()

cv2.imshow('frame', img)

cv2.waitKey(0)