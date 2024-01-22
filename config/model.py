from typing import List
from copy import deepcopy

import numpy as np

from ._model import digit_centroids


class Model:
    def __init__(self, 
                 image_name: str,
                 max_width: int = 0,
                 max_height: int = 0,
                 horizontals: List[int] = [],
                 verticals: List[int] = [],
                 matrix: List[List[int]] = [],
                 cells_y: int = 0,
                 cells_x: int = 0,
                 ):
        # Номера пикселей вертикальных и горизонтальных линий
        self.horizontals = horizontals
        self.verticals = verticals
        self.matrix = matrix
        # Специцальная матрица для записи в excel
        self.special_matrix = None
        self.image_name = image_name
        self.max_width = max_width
        self.max_height = max_height
        self.cells_y = cells_y
        self.cells_x = cells_x

        self.digits = digit_centroids

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
    
    def update_special_matrix_index(self) -> None:
        self.special_matrix = deepcopy(self.matrix)
        index = 1
        delete_indexes = []
        for row in self.special_matrix:
            if any(row):
                row.insert(0, index)
                index += 1
            else:
                delete_indexes.append(index-1)
        for index in delete_indexes:
            self.special_matrix.pop(index)
        self.special_matrix.insert(0, [None, *range(self.cells_x)])
