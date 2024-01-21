from typing import List


class Model:
    def __init__(self, 
                 horizontals: List[int] = [],
                 verticals: List[int] = [],
                 ):
        # Номера пикселей вертикальных и горизонтальных линий
        self.horizontals = horizontals
        self.verticals = verticals

    # Singleton 
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Model, cls).__new__(cls)

        return cls.instance