from typing import List

import cv2

from .process import process_frame, process_video
from ._frame import visualize_frame
from config import config, Model


def run(image_file=None, video_file=None, image_files=[], *args, **kwargs) -> Model | List[Model]:
    model_list = []
    model = None
    if image_file:
        image = cv2.imread(image_file).copy()
        model = process_frame(image=image, config=config, image_name=image_file)
        model.update_special_matrix_index()
        if config.visualize:
            visualize_frame(image, model, config)
    
    if len(image_files):
        for image_name in image_files:
            image = cv2.imread(image_name).copy()
            temp_model = process_frame(image=image, config=config, image_name=image_name)
            temp_model.update_special_matrix_index()
            model_list.append(temp_model)
            if config.visualize:
                visualize_frame(image, temp_model, config)

    return model or model_list
    
    return "Завершение просмотра..."
