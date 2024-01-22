from copy import copy
from itertools import product

import cv2
import numpy as np
import skimage.measure as sm
from scipy.spatial import distance_matrix

from config import Config
from config import Model


def _check_cell(image: np.ndarray, y1, y2, x1, x2, diff_y=0, diff_x=0) -> np.ndarray | None:
    if abs(y2 - y1) < diff_y or abs(x2 - x1) < diff_x:
        return None
    
    # ПОДПРАВЬ ЗДЕСЬ, ЕСЛИ БУДУТ ПРОБЛЕМЫ
    return image[y1+2:y2-1, x1+2:x2-1]


# Обработка кадра без визуализация
def process_frame(image: np.ndarray, config: Config, *args, **kwargs) -> Model:
    model = Model()

    # y, x и rgb. Будет использоваться суммирование по осям, поэтому меняем y и x местами
    max_vertical, max_horizontal, max_channels = image.shape
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresholded = cv2.threshold(gray, config.thr_white_color_cell, 255, cv2.THRESH_BINARY_INV)[1]
    
    low_row = cv2.threshold(gray, config.thr_black_color_cell, 255, cv2.THRESH_BINARY_INV)[1]
    low_sum = low_row.sum(1) / 255
    low_sum[low_sum < config.thr_horizontal * max_horizontal] = 0
    low = np.array([index for index, val in enumerate(low_sum) if val > 0], dtype=config.TYPE_OF_SIZE)[-1]
    # Добавляем нижний ряд в маску нашу
    thresholded[low:, :] = low_row[low:, :]
    thresholded = model.add_frame(thresholded)
    
    # Количество пикселей по вертикали
    y_sum = thresholded.sum(1) / 255
    y_sum[y_sum < config.thr_horizontal * max_horizontal] = 0
    # Индексы горизонтальных линий
    y = np.array([index for index, val in enumerate(y_sum) if val > 0], dtype=config.TYPE_OF_SIZE)
    diff_y = np.diff(y)
    # Число клеток по вертикали
    cells_y = len(diff_y[config.thr_cell_y_min < diff_y])

    # Динамическое обновление высоты линий по вертикали
    config.update_thr_vertical(cells_y - 2, max_vertical)

    # Количество пикселей по горизонтали
    x_sum = thresholded.sum(0) / 255
    x_sum[x_sum < config.thr_vertical * max_vertical] = 0
    # Индексы вертикальных линий
    x = np.array([index for index, val in enumerate(x_sum) if val > 0], dtype=config.TYPE_OF_SIZE)
    diff_x = np.diff(x)
    # Число клеток по горизонтали
    cells_x = len(diff_x[config.thr_cell_x_min < diff_x])

    # Необязательная часть
    mask = np.zeros_like(thresholded)
    mask[y, :] = 255
    mask[:, x] = 255
    # Удаляем лишние участки линий
    mask = np.where(thresholded, mask, thresholded)
    model.image = low_row

    model.verticals = list(x)
    model.horizontals = list(y)
    model.set_matrix_size(cells_y, cells_x)

    # Рассматриваем попарно вертикали и горизонтали, вырезая тем самым ячейки
    x_slides = np.lib.stride_tricks.sliding_window_view(x, 2)
    y_slides = np.lib.stride_tricks.sliding_window_view(y, 2)
    index = 0
    last = None
    last_label = None
    for y, x in product(y_slides, x_slides):
        cell = _check_cell(low_row, *y, *x, diff_x=config.thr_cell_x_min, diff_y=config.thr_cell_y_min)
        if cell is not None:
            if cell.any():
                label, num = sm.label(cell, return_num=True)
                digits = []
                for region in sm.regionprops(label):
                    for key, val in model.digits.items():
                        # if index == 2:
                        #     print(np.round(region.inertia_tensor) == np.round(val))
                        #     # print(region.inertia_tensor, val)
                        if (np.round(region.centroid_local*config.scale_to_diff) == 
                            np.round(np.array(val)*config.scale_to_diff)).all():
                            digits.append(key)

                if len(digits):
                    digits = int("".join(digits))
                else:
                    digits = None

                model.matrix[index // cells_x][index % cells_x] = digits
                # if index == 7:
                #     last = cell
                #     last_label = label
                
            index += 1
    for row in model.matrix:
        print(row)
    # for region in sm.regionprops(last_label):
    #     print(region.centroid_local)

    return thresholded

# Только визуализация модели на одно изображение
def visualize_frame(image: np.ndarray, 
                    model: Model, config: Config) -> np.ndarray:  
    if model.image is not None:
        cv2.imshow("Visualize", model.image)
    if model.ext_image is not None:
        cv2.imshow("Extended", model.ext_image)
    while True:
        k = cv2.waitKey(10) & 0xFF
        if (k == ord('q')):
            break

    cv2.destroyAllWindows()