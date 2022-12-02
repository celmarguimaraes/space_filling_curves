class Rectangle:
    '''Área da curva Pseudo Hilbert em forma de retângulo'''
    x1: int
    x2: int
    y1: int
    y2: int
    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def __str__(self) -> str:
        return f'{self.x1}, {self.y1} -> {self.x2}, {self.y2}'