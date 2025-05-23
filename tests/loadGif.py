import glob
import random

import cv2
import numpy as np

image_path_list = glob.glob("datasets/car/masks/*.gif")
image_path = random.choice(image_path_list)
print(image_path)
gif = cv2.VideoCapture(image_path)

frame_count = 0
image_list = []
success = True
while success:
    success, image = gif.read()
    if success:
        frame_count += 1
        image_list.append(image)
print(frame_count)
if len(image_list) > 0:
    print([x.shape for x in image_list])