from typing import List

import numpy as np

from ._model import digit_centroids


class Model:
    def __init__(self, 
                 horizontals: List[int] = [],
                 verticals: List[int] = [],
                 matrix: List[List[int]] = [],
                 ):
        # Номера пикселей вертикальных и горизонтальных линий
        self.horizontals = horizontals
        self.verticals = verticals
        self.matrix = matrix

        self.image = None
        self.ext_image = None

        self.digits = digit_centroids

    # Singleton 
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Model, cls).__new__(cls)

        return cls.instance
    
    # Добавление границ
    def add_frame(self, image: np.ndarray) -> np.ndarray:
        frame = image.copy()
        y, x = frame.shape
        frame[0, :] = 255
        frame[y - 1, :] = 255
        frame[:, 0] = 255
        frame[:, x - 1] = 255
        
        return frame
    
    def set_matrix_size(self, h: int, w: int) -> None:
        self.matrix = [[None for _ in range(w)] for _ in range(h)]