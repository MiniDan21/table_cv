import numpy as np

from config import Config
from config import Model
from ._frame import process_frame


# Специальный класс для хранения состояния при обработки видео
class VideoState:
    def __init__(self):
        pass # Поля для описания состояния

# Для обработки видео используем класс, 
# т.к. мы должны хранить информациюю с предыдущих кадров через состояние
class VideoProcessor:
    def __init__(self, config: Config):
        self.config = config
        self.state = VideoState() # Состояние обработки видео
   
    def update_state(self, model) -> Model:
        pass  # Обновляем self.state и возвращаем исправленный model

    # В отличии от функции process_frame, в методе 
    # мы используем дополнительную обработку по состоянию VideoState
    def process_frame(self, frame: np.ndarray):
        model = process_frame(frame, self.config)
        # Обрабатываем model с помощью VideoState
        processed_model = self.update_state(model)
        return processed_model