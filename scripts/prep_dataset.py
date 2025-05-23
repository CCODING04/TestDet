import glob
import os
import sys

import cv2
from rich.progress import Progress
from sklearn.model_selection import train_test_split


def main():
    data_dir = sys.argv[1].strip()
    image_dir = os.path.join(data_dir, "images")
    label_dir = os.path.join(data_dir, "labels")
    mask_dir = os.path.join(data_dir, "masks")
    image_path_list = glob.glob(os.path.join(image_dir, "*.jpg"))
    with Progress() as progress:
        progress.add_task('generate data info ...', len(image_path_list))


if __name__ == "__main__":
    main()