from typing import List

from config import Model, config
from ._frame import process_frame


test_dataset_images = []
test_dataset_answers = []

# Вычисление метрик качества на тестовой выборке
def estimate_metrics(predictions: List[Model], ground_truth: List[Model]):
    pass

predictions = []
for image in test_dataset_images:
    predictions.append(process_frame(image, config))

estimate_metrics(predictions, test_dataset_answers)