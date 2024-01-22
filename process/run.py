import cv2

from .process import process_frame, process_video
from ._frame import visualize_frame
from config import Config, Model


config = Config()
model = Model()

def run(image_file=None, video_file=None, image_files=[],  *args, **kwargs):
    try:
        if image_file:
            image = cv2.imread(image_file).copy()
            frame = process_frame(image=image, config=config)
            visualize_frame(frame, model, config)
        
        if len(image_files):
            for image_name in image_files:
                image = cv2.imread(image_name).copy()
                frame = process_frame(image=image, config=config)

    except Exception as e:
        print(e)
    
    return "Завершение просмотра..."
