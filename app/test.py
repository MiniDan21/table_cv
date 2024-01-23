from typing import List

from config import Model, config
from process import process_frame
from .files_utils import read_xlsx_file, path_array
from .output import print_green, print_red


# Вычисление метрик качества на тестовой выборке
def estimate_metrics(predictions: List[Model], ground_truth: List[Model], *args, **kwargs):
    for prediction, truth in zip(predictions, ground_truth):
        truth = list(map(list, truth))
        if prediction.special_matrix == truth:
            print_green(prediction.image_name + " - Тест пройден")
        else:
            print_red(prediction.image_name + " - Произошла ошибка в тесте")
