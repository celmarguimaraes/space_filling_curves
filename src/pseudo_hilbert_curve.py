import math
from src.curve import Curve
from typing import List
from src.curve_utils.coordinate import Coordinate
from src.curve_utils.dimension import Dimension
from src.curve_utils.rectangle import Rectangle

class PseudoPeanoHilbertCurve(Curve):
    UP: int = 0
    RIGHT: int = 1
    DOWN: int = 2
    LEFT: int = 3

    TOP_RIGHT: int = UP
    BOTTOM_RIGHT: int = RIGHT
    BOTTOM_LEFT: int = DOWN
    TOP_LEFT: int = LEFT

    CLOCKWISE = True
    COUNTER_CLOCKWISE = not CLOCKWISE

    map: List[List[int]]
    map_d_to_xy: List[Coordinate]

    def __init__(self, number_of_elements: int, dimension: Dimension = None) -> None:
        self.number_of_elements = number_of_elements
        if dimension is None:
            self.dimension = self.define_dimension(number_of_elements)
        else:
            self.dimension = dimension
        if dimension:
            self.dimension.x = dimension.x
            self.dimension.y = dimension.y
        self.map = self.fill_map(self.dimension)
        self.map_d_to_xy = self.fill_map_d_to_xy(number_of_elements)
    
    def fill_map(self, dimension: Dimension) -> List:
        self.map = [[0 for _ in range(dimension.y)] for _ in range(dimension.x)]
        self.recursiveFillMap(Rectangle(0, 0, dimension.x - 1, dimension.y - 1), False, 0, 0)
        return self.map

    def recursiveFillMap(self, r: Rectangle, senseOfRotation: bool, direction: int, d: int):
        print(f'recursive_fill_map {r} {senseOfRotation}')
        xStart=r.x1
        yStart=r.y1
        
        if ((direction == self.UP and senseOfRotation == self.COUNTER_CLOCKWISE) or
                (direction == self.LEFT and senseOfRotation == self.CLOCKWISE)):
            xStart=r.x1
            yStart=r.y1
        elif ((direction == self.LEFT and senseOfRotation == self.COUNTER_CLOCKWISE) or
                (direction == self.DOWN and senseOfRotation == self.CLOCKWISE)):
            xStart=r.x1
            yStart=r.y2
        elif ((direction==self.DOWN and senseOfRotation==self.COUNTER_CLOCKWISE) or
                (direction==self.RIGHT and senseOfRotation==self.CLOCKWISE)):
            xStart=r.x2
            yStart=r.y2
        elif ((direction==self.RIGHT and senseOfRotation==self.COUNTER_CLOCKWISE) or
                (direction==self.UP and senseOfRotation==self.CLOCKWISE)):
            xStart=r.x2
            yStart=r.y1
        
        deltaX = int(abs(r.x2 - r.x1) + 1)
        deltaY = int(abs(r.y2 - r.y1) + 1)

        if (deltaX == 1 and deltaY == 1):
            print('deltaX=1, deltaY=1')
            self.map[r.x1][r.y1] = d
            d += 1

        elif (deltaX == 1 and deltaY > 1):
            print('deltaX=1, deltaY>1')
            sentidoY=1
            if (direction==self.DOWN or
                    (direction==self.RIGHT and senseOfRotation==self.COUNTER_CLOCKWISE) or
                    (direction==self.LEFT and senseOfRotation==self.CLOCKWISE)):
                sentidoY=1
                yStart=r.y1
            elif (direction==self.UP or
                    (direction==self.RIGHT and senseOfRotation==self.CLOCKWISE) or
                    (direction==self.LEFT and senseOfRotation==self.COUNTER_CLOCKWISE)):
                sentidoY=-1
                yStart=r.y2
            
            yEnd = int(r.y2) if yStart == r.y1 else int(r.y1)
            y = yStart
            while y != yEnd+sentidoY:
                self.map[r.x1][y] = d
                d += 1
                y += sentidoY

        elif (deltaX > 1 and deltaY == 1):
            print('deltaX>1, deltaY=1')
            sentidoX=int(1)
            if (direction==self.RIGHT or
                    (direction==self.UP and senseOfRotation==self.COUNTER_CLOCKWISE) or
                    (direction==self.DOWN and senseOfRotation==self.CLOCKWISE)):
                sentidoX=1
                xStart=r.x1
            elif (direction==self.LEFT or
                    (direction==self.UP and senseOfRotation==self.CLOCKWISE) or
                    (direction==self.DOWN and senseOfRotation==self.COUNTER_CLOCKWISE)):
                sentidoX=-1
                xStart=r.x2
            
            xEnd = int(r.x2) if xStart == r.x1 else int(r.x1)
            x = xStart
            while x != xEnd+sentidoX:
                self.map[x][r.y1] = d
                d+= 1
                x += sentidoX

        elif (deltaX == 2 and deltaY >= 2):
            print('deltaX=2, deltaY>=2')
            if ((xStart == r.x1 and yStart == r.y1 and senseOfRotation==self.COUNTER_CLOCKWISE)
            or  (xStart == r.x2 and yStart == r.y1 and senseOfRotation==self.CLOCKWISE)
            or  (xStart == r.x2 and yStart == r.y2 and senseOfRotation==self.COUNTER_CLOCKWISE)
            or  (xStart == r.x1 and yStart == r.y2 and senseOfRotation==self.CLOCKWISE)):
                sentidoY = int(1) if yStart == r.y1 else int(-1)
                yEnd = int(r.y2) if yStart == r.y1 else int(r.y1)
                x = int(xStart)
                y = yStart
                while y != yEnd+sentidoY:
                    self.map[x][y] = d
                    d+= 1
                    y += sentidoY
                x = int(r.x2) if xStart == r.x1 else int(r.x1)
                sentidoY = -sentidoY
                y = int(yEnd)
                while y != yStart+sentidoY:
                    self.map[x][y] = d
                    d += 1
                    y += sentidoY

            else:
                sentidoY = int(1) if yStart == r.y1 else int(-1)
                sentidoX = int(1) if xStart == r.x1 else int(-1)
                yEnd = int(r.y2) if yStart == r.y1 else int(r.y1)
                y = int(yStart)
                while y != int(yEnd+sentidoY):
                    if y == yEnd:
                        sentidoX = -sentidoX
                    if sentidoX == 1:
                        self.map[r.x1][y] = d
                        d += 1
                        self.map[r.x2][y] = d
                        d += 1
                    else:
                        self.map[r.x2][y] = d
                        d += 1
                        self.map[r.x1][y] = d
                        d += 1
                    y += sentidoY

        
        elif (deltaX >= 2 and deltaY == 2):
            print('deltaX>=2, deltaY=2')
            if ((yStart == r.y1 and xStart == r.x1 and senseOfRotation==self.CLOCKWISE)
             or (yStart == r.y2 and xStart == r.x1 and senseOfRotation==self.COUNTER_CLOCKWISE)
             or (yStart == r.y2 and xStart == r.x2 and senseOfRotation==self.CLOCKWISE)
             or (yStart == r.y1 and xStart == r.x2 and senseOfRotation==self.COUNTER_CLOCKWISE)):
                sentidoX = int(1) if xStart == r.x1 else int(-1)
                xEnd = int(r.x2) if xStart == r.x1 else int(r.x1)
                y = int(yStart)
                x = int(xStart)
                while x != xEnd+sentidoX:
                    self.map[x][y] = d
                    d += 1
                    x += sentidoX
                y = int(r.y2) if yStart == r.y1 else int(r.y1)
                sentidoX = -sentidoX
                x = int(xEnd)
                while x != xStart+sentidoX:
                    self.map[x][y] = d
                    d += 1
                    x += sentidoX

            else:
                sentidoX = 1 if xStart == r.x1 else -1
                sentidoY = 1 if yStart == r.y1 else -1
                xEnd = int(r.x2) if xStart == r.x1 else int(r.x1)
                x = int(xStart)
                while x != xEnd+sentidoX:
                    if x == xEnd:
                        sentidoY = -sentidoY
                    if sentidoY == 1:
                        self.map[x][r.y1] = d
                        d += 1
                        self.map[x][r.y2] = d
                        d += 1
                    else:
                        self.map[x][r.y2] = d
                        d += 1
                        self.map[x][r.y1] = d
                        d += 1
                    x += sentidoX

        elif (deltaX > 2 and deltaY > 2):
            print('deltaX>2, deltaY>2')
            
            xMean = int((r.x1+r.x2) // 2)
            yMean = int((r.y1+r.y2) // 2)
            currentDirection = int(direction)
            
            topLeft = Rectangle(r.x1,r.y1,xMean,yMean)
            bottomLeft = Rectangle(r.x1,yMean+1,xMean,r.y2)
            bottomRight = Rectangle(xMean+1,yMean+1,r.x2,r.y2)
            topRight = Rectangle(xMean+1,r.y1,r.x2,yMean)
            
            rectangles = []
            rectangles.append(topRight)
            rectangles.append(bottomRight)
            rectangles.append(bottomLeft)
            rectangles.append(topLeft)
            

            currentRectangleIndex = int(0)
            currentRectangle: Rectangle = None
            rotationStep = 1
            if (not senseOfRotation):
                currentDirection=self.rotateDirection(currentDirection, -1)
                rotationStep=-1
            else:
                rotationStep=1
            
            currentRectangleIndex = int(currentDirection%4)
            currentRectangle=rectangles[currentRectangleIndex]
            d=self.recursiveFillMap(currentRectangle, not senseOfRotation, 
              self.rotateDirection(direction=direction, clockwise=senseOfRotation, step=1),d)
            
            currentRectangleIndex=self.rotateDirection(direction=currentDirection, clockwise_step=rotationStep)
            currentRectangle=rectangles[currentRectangleIndex]
            d=self.recursiveFillMap(currentRectangle,senseOfRotation,direction,d)
            
            currentRectangleIndex=self.rotateDirection(direction=currentDirection, clockwise_step=rotationStep*2)
            currentRectangle=rectangles[currentRectangleIndex]
            d=self.recursiveFillMap(currentRectangle,senseOfRotation,direction,d)
            
            currentRectangleIndex=self.rotateDirection(direction=currentDirection, clockwise_step=rotationStep*3)
            currentRectangle=rectangles[currentRectangleIndex]
            d=self.recursiveFillMap(currentRectangle,not senseOfRotation,
              self.rotateDirection(direction=direction, clockwise=not senseOfRotation, step=1),d)
            
        else:
            print('There was a problem with creating pseudo Peano-Hilbert curve')
        # print('d: ',d)
        return d

            
    def rotateDirection(self, direction: int, clockwise_step: int = None, clockwise: bool = None, step: int = None) -> int:
        if clockwise_step:
            return (direction + clockwise_step + 4) % 4
        else:
            if clockwise:
                return (direction + step) % 4
            else:
                return (direction - step + 4) % 4

    def fill_map_d_to_xy(self, number_of_elements: int):
        self.map_d_to_xy = [None for _ in range(number_of_elements)]
        d = None
        for y in range(0, self.dimension.y):
            for x in range(0, self.dimension.x):
                d = self.get_d(x, y)
                if (d >= 0 and d < number_of_elements):
                    self.map_d_to_xy[d] = Coordinate(x, y)
        return self.map_d_to_xy

    def define_dimension(self, number_of_elements: int) -> Dimension:
        '''Define as dimensões da área a ser preenchida  de acordo com o número de elementos'''
        d = math.ceil(math.sqrt(number_of_elements))
        return Dimension(d, d)

    def get_coordinate(self, d: int) -> Coordinate:
        '''Retorna as coordenadas de um ponto da curva de Pseudo-Hilbert'''
        return self.map_d_to_xy[d]

    def get_d(self, x: int, y: int) -> int:
        '''Retorna a distância de um ponto da curva de Pseudo-Hilbert'''
        if x >= len(self.map) or y >= len(self.map[0]) or x < 0 or y < 0:
            return -1
        else:
            return self.map[x][y]

    def get_number_of_elements(self):
        return self.number_of_elements

    def get_dimension(self):
        return self.dimension

    def print(self):
        d = self.get_dimension()
        for y in range(0, d.y):
            for x in range(0, d.x):
                print(self.get_d(x, y), end="\t")
            print()