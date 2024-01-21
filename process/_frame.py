import numpy as np

from config import Config
from config import Model


# Обработка кадра без визуализация
def process_frame(image: np.ndarray, config: Config) -> Model:
    pass

# заглушка - удалить после тестирования
def process_frame(*args, **kwargs):
    pass

# Только визуализация модели на одно изображение
def visualize_frame(image: np.ndarray, 
                    model: Model, config: Config) -> np.ndarray:  
    pass