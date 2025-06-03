from ultralytics import YOLO

path = 'C:/Users/UAE LAPTOP BAZAR/Documents/DevyJonesLocker/python-image/Image_processing/object-detection-YOLO/colab_runs/detect/train/weights/best.pt'
model = YOLO(path)

video = 'C:/Users/UAE LAPTOP BAZAR/Documents/DevyJonesLocker/python-image/Image_processing/object-detection-YOLO/content/alpaca_vid1.mp4'

results = model.predict(video, show=True)