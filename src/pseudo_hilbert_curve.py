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

    def __init__(self, number_of_elements: int, dimension: Dimension = None, direction: int = 0, sense_of_rotation: bool = False) -> None:
        self.number_of_elements = number_of_elements
        if dimension is None:
            self.dimension = self.define_dimension(number_of_elements)
        else:
            self.dimension = dimension
        if dimension:
            self.dimension.x = dimension.x
            self.dimension.y = dimension.y
        self.map = self.fill_map(self.dimension, direction, sense_of_rotation)
        self.map_d_to_xy = self.fill_map_d_to_xy(number_of_elements)

    def fill_map(self, dimension: Dimension, direction: int, sense_of_rotation: bool) -> List:
        self.map = [[0 for _ in range(dimension.y)] for _ in range(dimension.x)]
        self.recursive_fill_map(Rectangle(0, 0, dimension.x - 1, dimension.y - 1), sense_of_rotation=sense_of_rotation, direction=direction, d=0)
        return self.map

    def recursive_fill_map(self, r: Rectangle, sense_of_rotation: bool, direction: int, d: int):
        x_start = r.x1
        y_start = r.y1

        if ((direction == self.UP and sense_of_rotation == self.COUNTER_CLOCKWISE) or
                (direction == self.LEFT and sense_of_rotation == self.CLOCKWISE)):
            x_start = r.x1
            y_start = r.y1
        elif ((direction == self.LEFT and sense_of_rotation == self.COUNTER_CLOCKWISE) or
                (direction == self.DOWN and sense_of_rotation == self.CLOCKWISE)):
            x_start = r.x1
            y_start = r.y2
        elif ((direction == self.DOWN and sense_of_rotation == self.COUNTER_CLOCKWISE) or
                (direction == self.RIGHT and sense_of_rotation == self.CLOCKWISE)):
            x_start = r.x2
            y_start = r.y2
        elif ((direction == self.RIGHT and sense_of_rotation == self.COUNTER_CLOCKWISE) or
                (direction == self.UP and sense_of_rotation == self.CLOCKWISE)):
            x_start = r.x2
            y_start = r.y1

        delta_x = abs(r.x2 - r.x1) + 1
        delta_y = abs(r.y2 - r.y1) + 1

        if (delta_x == 1 and delta_y == 1):
            self.map[r.x1][r.y1] = d
            d += 1

        elif (delta_x == 1 and delta_y > 1):
            sentido_y = 1
            if (direction == self.DOWN or
                    (direction == self.RIGHT and sense_of_rotation == self.COUNTER_CLOCKWISE) or
                    (direction == self.LEFT and sense_of_rotation == self.CLOCKWISE)):
                sentido_y = 1
                y_start = r.y1
            elif (direction == self.UP or
                    (direction == self.RIGHT and sense_of_rotation == self.CLOCKWISE) or
                    (direction == self.LEFT and sense_of_rotation == self.COUNTER_CLOCKWISE)):
                sentido_y = -1
                y_start = r.y2

            y_end = r.y2 if y_start == r.y1 else r.y1
            y = y_start
            while y != y_end + sentido_y:
                self.map[r.x1][y] = d
                d += 1
                y += sentido_y

        elif (delta_x > 1 and delta_y == 1):
            sentido_x = 1
            if ((direction == self.RIGHT) or
                    (direction == self.UP and sense_of_rotation == self.COUNTER_CLOCKWISE) or
                    (direction == self.DOWN and sense_of_rotation == self.CLOCKWISE)):
                sentido_x = 1
                x_start = r.x1
            elif (direction == self.LEFT or
                    (direction == self.UP and sense_of_rotation == self.CLOCKWISE) or
                    (direction == self.DOWN and sense_of_rotation == self.COUNTER_CLOCKWISE)):
                sentido_x = -1
                x_start = r.x2

            x_end = r.x2 if x_start == r.x1 else r.x1
            x = x_start
            while x != x_end + sentido_x:
                self.map[x][r.y1] = d
                d += 1
                x += sentido_x

        elif (delta_x == 2 and delta_y >= 2):
            if ((x_start == r.x1 and y_start == r.y1 and sense_of_rotation == self.COUNTER_CLOCKWISE)
            or (x_start == r.x2 and y_start == r.y1 and sense_of_rotation == self.CLOCKWISE)
            or (x_start == r.x2 and y_start == r.y2 and sense_of_rotation == self.COUNTER_CLOCKWISE)
            or (x_start == r.x1 and y_start == r.y2 and sense_of_rotation == self.CLOCKWISE)):
                sentido_y = 1 if y_start == r.y1 else -1
                y_end = r.y2 if y_start == r.y1 else r.y1
                x = x_start
                y = y_start
                while y != y_end + sentido_y:
                    self.map[x][y] = d
                    d += 1
                    y += sentido_y
                x = r.x2 if x_start == r.x1 else r.x1
                sentido_y = -sentido_y
                y = y_end
                while y != y_start + sentido_y:
                    self.map[x][y] = d
                    d += 1
                    y += sentido_y

            else:
                sentido_y = 1 if y_start == r.y1 else -1
                sentido_x = 1 if x_start == r.x1 else -1
                y_end = r.y2 if y_start == r.y1 else r.y1
                y = y_start
                while y != y_end + sentido_y:
                    if y == y_end:
                        sentido_x = -sentido_x
                    if sentido_x == 1:
                        self.map[r.x1][y] = d
                        d += 1
                        self.map[r.x2][y] = d
                        d += 1
                    else:
                        self.map[r.x2][y] = d
                        d += 1
                        self.map[r.x1][y] = d
                        d += 1
                    y += sentido_y

        elif (delta_x >= 2 and delta_y == 2):
            if ((y_start == r.y1 and x_start == r.x1 and sense_of_rotation == self.CLOCKWISE)
             or (y_start == r.y2 and x_start == r.x1 and sense_of_rotation == self.COUNTER_CLOCKWISE)
             or (y_start == r.y2 and x_start == r.x2 and sense_of_rotation == self.CLOCKWISE)
             or (y_start == r.y1 and x_start == r.x2 and sense_of_rotation == self.COUNTER_CLOCKWISE)):
                sentido_x = 1 if x_start == r.x1 else -1
                x_end = r.x2 if x_start == r.x1 else r.x1
                y = y_start
                x = x_start
                while x != x_end+sentido_x:
                    self.map[x][y] = d
                    d += 1
                    x += sentido_x
                y = r.y2 if y_start == r.y1 else r.y1
                sentido_x = -sentido_x
                x = x_end
                while x != x_start+sentido_x:
                    self.map[x][y] = d
                    d += 1
                    x += sentido_x

            else:
                sentido_x = 1 if x_start == r.x1 else -1
                sentido_y = 1 if y_start == r.y1 else -1
                x_end = r.x2 if x_start == r.x1 else r.x1
                x = x_start
                while x != x_end+sentido_x:
                    if x == x_end:
                        sentido_y = -sentido_y
                    if sentido_y == 1:
                        self.map[x][r.y1] = d
                        d += 1
                        self.map[x][r.y2] = d
                        d += 1
                    else:
                        self.map[x][r.y2] = d
                        d += 1
                        self.map[x][r.y1] = d
                        d += 1
                    x += sentido_x

        elif (delta_x == 3 and delta_y == 3):
            if direction == self.UP and sense_of_rotation == self.CLOCKWISE:
                '''
                _____
                     |     |
                 ____|     |
                |          |
                |__________|
                '''
                self.map[x_start][y_start] = d
                d += 1
                self.map[x_start][y_start + 1] = d
                d += 1
                self.map[x_start][y_start + 2] = d
                d += 1
                self.map[x_start - 1][y_start + 2] = d
                d += 1
                self.map[x_start - 2][y_start + 2] = d
                d += 1
                self.map[x_start - 2][y_start + 1] = d
                d += 1
                self.map[x_start - 1][y_start + 1] = d
                d += 1
                self.map[x_start - 1][y_start] = d
                d += 1
                self.map[x_start - 2][y_start] = d
                d += 1
            elif direction == self.UP and sense_of_rotation == self.COUNTER_CLOCKWISE:
                '''
                _____
                     |     |
                 ____|     |
                |          |
                |__________|
                '''
                self.map[x_start][y_start] = d
                d += 1
                self.map[x_start + 1][y_start] = d
                d += 1
                self.map[x_start + 1][y_start + 1] = d
                d += 1
                self.map[x_start][y_start + 1] = d
                d += 1
                self.map[x_start][y_start + 2] = d
                d += 1
                self.map[x_start + 1][y_start + 2] = d
                d += 1
                self.map[x_start + 2][y_start + 2] = d
                d += 1
                self.map[x_start + 2][y_start + 1] = d
                d += 1
                self.map[x_start + 2][y_start] = d
                d += 1
            elif direction == self.RIGHT and sense_of_rotation == self.CLOCKWISE:
                '''
                 ____
                |     |    |
                |     |____|
                |
                |
                |___________
                '''
                self.map[x_start][y_start] = d
                d += 1
                self.map[x_start - 1][y_start] = d
                d += 1
                self.map[x_start - 2][y_start] = d
                d += 1
                self.map[x_start - 2][y_start - 1] = d
                d += 1
                self.map[x_start - 2][y_start - 2] = d
                d += 1
                self.map[x_start - 1][y_start - 2] = d
                d += 1
                self.map[x_start - 1][y_start - 1] = d
                d += 1
                self.map[x_start][y_start - 1] = d
                d += 1
                self.map[x_start][y_start - 2] = d
                d += 1
            elif direction == self.RIGHT and sense_of_rotation == self.COUNTER_CLOCKWISE:
                '''
                 ____
                |     |    |
                |     |____|
                |
                |
                |___________
                '''
                self.map[x_start][y_start] = d
                d += 1
                self.map[x_start][y_start + 1] = d
                d += 1
                self.map[x_start - 1][y_start + 1] = d
                d += 1
                self.map[x_start - 1][y_start] = d
                d += 1
                self.map[x_start - 2][y_start] = d
                d += 1
                self.map[x_start - 2][y_start + 1] = d
                d += 1
                self.map[x_start - 2][y_start + 2] = d
                d += 1
                self.map[x_start - 1][y_start + 2] = d
                d += 1
                self.map[x_start][y_start + 2] = d
                d += 1
            elif direction == self.DOWN and sense_of_rotation == self.CLOCKWISE:
                '''
                 _____________
                |             |
                |       ______|
                |      |
                |      |______
                '''
                self.map[x_start][y_start] = d
                d += 1
                self.map[x_start][y_start - 1] = d
                d += 1
                self.map[x_start][y_start - 2] = d
                d += 1
                self.map[x_start + 1][y_start - 2] = d
                d += 1
                self.map[x_start + 2][y_start - 2] = d
                d += 1
                self.map[x_start + 2][y_start - 1] = d
                d += 1
                self.map[x_start + 1][y_start - 1] = d
                d += 1
                self.map[x_start + 1][y_start] = d
                d += 1
                self.map[x_start + 2][y_start] = d
                d += 1
            elif direction == self.DOWN and sense_of_rotation == self.COUNTER_CLOCKWISE:
                '''
                 _____________
                |             |
                |       ______|
                |      |
                |      |______
                '''
                self.map[x_start][y_start] = d
                d += 1
                self.map[x_start - 1][y_start] = d
                d += 1
                self.map[x_start - 1][y_start - 1] = d
                d += 1
                self.map[x_start][y_start - 1] = d
                d += 1
                self.map[x_start][y_start - 2] = d
                d += 1
                self.map[x_start - 1][y_start - 2] = d
                d += 1
                self.map[x_start - 2][y_start - 2] = d
                d += 1
                self.map[x_start - 2][y_start - 1] = d
                d += 1
                self.map[x_start - 2][y_start] = d
                d += 1
            elif direction == self.LEFT and sense_of_rotation == self.CLOCKWISE:
                '''
                ____________
                            |
                            |
                 ____       |
                |     |     |
                |     |_____|
                '''
                self.map[x_start][y_start] = d
                d += 1
                self.map[x_start + 1][y_start] = d
                d += 1
                self.map[x_start + 2][y_start] = d
                d += 1
                self.map[x_start + 2][y_start + 1] = d
                d += 1
                self.map[x_start + 2][y_start + 2] = d
                d += 1
                self.map[x_start + 1][y_start + 2] = d
                d += 1
                self.map[x_start + 1][y_start + 1] = d
                d += 1
                self.map[x_start][y_start + 1] = d
                d += 1
                self.map[x_start][y_start + 2] = d
                d += 1
            elif direction == self.LEFT and sense_of_rotation == self.COUNTER_CLOCKWISE:
                '''
                ____________
                            |
                            |
                 ____       |
                |     |     |
                |     |_____|
                '''
                self.map[x_start][y_start] = d
                d += 1
                self.map[x_start][y_start - 1] = d
                d += 1
                self.map[x_start + 1][y_start - 1] = d
                d += 1
                self.map[x_start + 1][y_start] = d
                d += 1
                self.map[x_start + 2][y_start] = d
                d += 1
                self.map[x_start + 2][y_start - 1] = d
                d += 1
                self.map[x_start + 2][y_start - 2] = d
                d += 1
                self.map[x_start + 1][y_start - 2] = d
                d += 1
                self.map[x_start][y_start - 2] = d
                d += 1
            else:
                raise Exception("Invalid sense of rotation or direction")

        elif (delta_x > 2 and delta_y > 2):
            x_mean = (r.x1+r.x2) // 2
            y_mean = (r.y1+r.y2) // 2
            current_direction = direction

            top_left = Rectangle(r.x1, r.y1, x_mean, y_mean)
            bottom_left = Rectangle(r.x1, y_mean+1, x_mean, r.y2)
            bottom_right = Rectangle(x_mean+1, y_mean+1, r.x2, r.y2)
            top_right = Rectangle(x_mean+1, r.y1, r.x2, y_mean)

            rectangles: List[Rectangle] = []
            rectangles.append(top_right)
            rectangles.append(bottom_right)
            rectangles.append(bottom_left)
            rectangles.append(top_left)

            current_rectangle_index = 0
            current_rectangle: Rectangle = None
            rotation_step = 1
            if (not sense_of_rotation):
                current_direction = self.rotate_rectangle_position(current_direction, -1)
                rotation_step = -1
            else:
                rotation_step = 1

            r1_direction = self.rotate_direction(direction=direction, clockwise=sense_of_rotation, step=1)
            r2_direction = direction
            r3_direction = direction
            r4_direction = self.rotate_direction(direction=direction, clockwise=not sense_of_rotation, step=1)

            # if direction == self.UP:
            #     if rectangles[0].get_width() == 1 and rectangles[1].get_width() == 1:
            #         r2_direction = self.rotate_direction(direction=direction, clockwise=sense_of_rotation, step=2)
            #     elif rectangles[1].get_height() == 1 and rectangles[2].get_height() == 1:
            #         r3_direction = self.rotate_direction(direction=direction, clockwise=sense_of_rotation, step=2)
            #     elif rectangles[2].get_width() == 1 and rectangles[3].get_width() == 1:
            #         r4_direction = self.rotate_direction(direction=direction, clockwise=not sense_of_rotation, step=2)
            #     else:
            #         pass
            # if direction == self.RIGHT:
            #     if rectangles[0].get_height() == 1 and rectangles[1].get_height() == 1:
            #         r2_direction = self.rotate_direction(direction=direction, clockwise=sense_of_rotation, step=2)
            #     elif rectangles[1].get_width() == 1 and rectangles[2].get_width() == 1:
            #         r3_direction = self.rotate_direction(direction=direction, clockwise=sense_of_rotation, step=2)
            #     elif rectangles[2].get_height() == 1 and rectangles[3].get_height() == 1:
            #         r4_direction = self.rotate_direction(direction=direction, clockwise=not sense_of_rotation, step=2)
            #     else:
            #         pass
            # if direction == self.DOWN:
            #     if rectangles[0].get_width() == 1 and rectangles[1].get_width() == 1:
            #         r2_direction = self.rotate_direction(direction=direction, clockwise=sense_of_rotation, step=2)
            #     elif rectangles[1].get_height() == 1 and rectangles[2].get_height() == 1:
            #         r3_direction = self.rotate_direction(direction=direction, clockwise=sense_of_rotation, step=2)
            #     elif rectangles[2].get_width() == 1 and rectangles[3].get_width() == 1:
            #         r4_direction = self.rotate_direction(direction=direction, clockwise=not sense_of_rotation, step=2)
            #     else:
            #         pass
            # if direction == self.LEFT:
            #     if rectangles[0].get_height() == 1 and rectangles[1].get_height() == 1:
            #         r2_direction = self.rotate_direction(direction=direction, clockwise=sense_of_rotation, step=2)
            #     elif rectangles[1].get_width() == 1 and rectangles[2].get_width() == 1:
            #         r3_direction = self.rotate_direction(direction=direction, clockwise=sense_of_rotation, step=2)
            #     elif rectangles[2].get_height() == 1 and rectangles[3].get_height() == 1:
            #         r4_direction = self.rotate_direction(direction=direction, clockwise=not sense_of_rotation, step=2)
            #     else:
            #         pass

            current_rectangle_index = current_direction % 4
            current_rectangle = rectangles[current_rectangle_index]
            d = self.recursive_fill_map(current_rectangle, not sense_of_rotation, r1_direction, d)

            current_rectangle_index = self.rotate_rectangle_position(direction=current_direction, clockwise_step=rotation_step)
            current_rectangle = rectangles[current_rectangle_index]
            d = self.recursive_fill_map(current_rectangle, sense_of_rotation, r2_direction, d)

            current_rectangle_index = self.rotate_rectangle_position(direction=current_direction, clockwise_step=rotation_step * 2)
            current_rectangle = rectangles[current_rectangle_index]
            d = self.recursive_fill_map(current_rectangle, sense_of_rotation, r3_direction, d)

            current_rectangle_index = self.rotate_rectangle_position(direction=current_direction, clockwise_step=rotation_step * 3)
            current_rectangle = rectangles[current_rectangle_index]
            d = self.recursive_fill_map(current_rectangle, not sense_of_rotation, r4_direction, d)

        else:
            pass
        return d

    def rotate_rectangle_position(self, direction, clockwise_step):
        return (direction + clockwise_step + 4) % 4

    def rotate_direction(self, direction: int, clockwise: bool = None, step: int = None) -> int:
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
