from typing import List

import numpy as np


class Config:
    def __init__(self, 
                 thr_white_color_cell: float = 215,
                 thr_black_color_cell: float = 100,
                 thr_horizontal: float = 0.8,
                 thr_vertical: float = 0.6,
                 thr_cell_y_min: int = 13,
                 thr_cell_y_max: int = 16,
                 thr_cell_x_min: int = 33,
                 scale_to_diff: int = 100,
                 visualize: bool = False,
                 ):
        self.visualize = visualize

        self.thr_white_color_cell = thr_white_color_cell
        self.thr_black_color_cell = thr_black_color_cell
        # Отношение числа обнаруженных пикселей в ряду(колонне) 
        # к общему числу пикселей в ряду (ширина и высота изображения)
        self.thr_horizontal = thr_horizontal
        self.thr_vertical = thr_vertical

        # Высота ячеек в пикселях
        self.thr_cell_y_min = thr_cell_y_min
        self.thr_cell_y_max = thr_cell_y_max
        # Ширина ячеек в пикселях
        self.thr_cell_x_min = thr_cell_x_min
        # Увеличение значений centroid для обнаружения разницы
        self.scale_to_diff = scale_to_diff

        self.TYPE_OF_SIZE = np.uint16

        self.IMAGES_DIR        = "images"
        self.VIDEOS_DIR        = "videos"
        self.OTHER_DIR         = "other"
        self.README_PATH       = "README.md"
        
        # Ссылки на Google Drive 
        self.GOOGLE_DRIVE_LINK = "https://drive.google.com/uc?id="
        self.LINK_IMAGES_ZIP   = self.GOOGLE_DRIVE_LINK + "17OmIJpegt1nPhw3_JNNT-azOfDqA2mj3"
        self.LINK_VIDEOS_ZIP   = ""
    
    # Singleton 
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)

        return cls.instance

    def update_thr_vertical(self, vertical_cells: int, height: int) -> None:
        self.thr_vertical = vertical_cells * self.thr_cell_y_min / height

config = Config(visualize=False)