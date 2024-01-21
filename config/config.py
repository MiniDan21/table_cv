from typing import List


class Config:
    def __init__(self, 
                 threshold: int = 2,
                 ):
        # Номера пикселей вертикальных и горизонтальных линий
        self.threshold = threshold

        self.IMAGES_DIR = "images"
        self.VIDEOS_DIR = "videos"
        self.README_PATH = "README.md"
        
        # Ссылки на Google Drive 
        self.GOOGLE_DRIVE_LINK = f"https://drive.google.com/uc?id={id}"
        self.LINK_IMAGES_ZIP = self.GOOGLE_DRIVE_LINK.format(id="17OmIJpegt1nPhw3_JNNT-azOfDqA2mj3")
        self.LINK_VIDEOS_ZIP = ""

    # Singleton 
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)

        return cls.instance