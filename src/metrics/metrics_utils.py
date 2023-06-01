from ..curve_utils.coordinate import Coordinate
from ..curve import Curve
from typing import List


def get_coord_neighbors(curve: Curve, coord: Coordinate) -> List[Coordinate]:
    if coord.get_x() == 0:
        if coord.get_y() == 0:
            return [Coordinate(coord.get_x() + 1, coord.get_y()), Coordinate(coord.get_x(), coord.get_y() + 1)]
        elif coord.get_y() == curve.dimension.y - 1:
            return [Coordinate(coord.get_x() + 1, coord.get_y()), Coordinate(coord.get_x(), coord.get_y() - 1)]
        else:
            return [Coordinate(coord.get_x() + 1, coord.get_y()), Coordinate(coord.get_x(), coord.get_y() + 1), Coordinate(coord.get_x(), coord.get_y() - 1)]
    elif coord.get_x() == curve.dimension.x - 1:
        if coord.get_y() == 0:
            return [Coordinate(coord.get_x() - 1, coord.get_y()), Coordinate(coord.get_x(), coord.get_y() + 1)]
        elif coord.get_y() == curve.dimension.y - 1:
            return [Coordinate(coord.get_x() - 1, coord.get_y()), Coordinate(coord.get_x(), coord.get_y() - 1)]
        else:
            return [Coordinate(coord.get_x() - 1, coord.get_y()), Coordinate(coord.get_x(), coord.get_y() + 1), Coordinate(coord.get_x(), coord.get_y() - 1)]
    elif coord.get_y() == 0:
        if coord.get_x() == 0:
            return [Coordinate(coord.get_x() + 1, coord.get_y()), Coordinate(coord.get_x(), coord.get_y() + 1)]
        elif coord.get_x() == curve.dimension.x - 1:
            return [Coordinate(coord.get_x() - 1, coord.get_y()), Coordinate(coord.get_x(), coord.get_y() + 1)]
        else:
            return [Coordinate(coord.get_x() + 1, coord.get_y()), Coordinate(coord.get_x() - 1, coord.get_y()), Coordinate(coord.get_x(), coord.get_y() + 1)]
    elif coord.get_y() == curve.dimension.y - 1:
        if coord.get_x() == 0:
            return [Coordinate(coord.get_x() + 1, coord.get_y()), Coordinate(coord.get_x(), coord.get_y() - 1)]
        elif coord.get_x() == curve.dimension.x - 1:
            return [Coordinate(coord.get_x() - 1, coord.get_y()), Coordinate(coord.get_x(), coord.get_y() - 1)]
        else:
            return [Coordinate(coord.get_x() + 1, coord.get_y()), Coordinate(coord.get_x() - 1, coord.get_y()), Coordinate(coord.get_x(), coord.get_y() - 1)]
    else:
        return [Coordinate(coord.get_x() + 1, coord.get_y()), Coordinate(coord.get_x() - 1, coord.get_y()), Coordinate(coord.get_x(), coord.get_y() + 1), Coordinate(coord.get_x(), coord.get_y() - 1)]
    

def get_d_neighbors(curve: Curve, d: int) -> List[int]:
    if d == 0:
        return [1]
    elif d == curve.get_number_of_elements() - 1:
        return [curve.get_number_of_elements() - 2]
    else:
        return [d - 1, d + 1]


def is_coord_neighbor(coord1: Coordinate, coord2: Coordinate) -> bool:
    if coord1.get_x() == coord2.get_x():
        if coord1.get_y() == coord2.get_y() + 1 or coord1.get_y() == coord2.get_y() - 1:
            return True
        else:
            return False
    elif coord1.get_y() == coord2.get_y():
        if coord1.get_x() == coord2.get_x() + 1 or coord1.get_x() == coord2.get_x() - 1:
            return True
        else:
            return False
    else:
        return False
    

def get_coord_neighbors_9(curve: Curve, coord: Coordinate) -> List[Coordinate]:
    coords = [
        Coordinate(coord.get_x() - 1, coord.get_y() - 1),
        Coordinate(coord.get_x() - 1, coord.get_y()),
        Coordinate(coord.get_x() - 1, coord.get_y() + 1), 
        Coordinate(coord.get_x(), coord.get_y() - 1),
        Coordinate(coord.get_x(), coord.get_y()),
        Coordinate(coord.get_x(), coord.get_y() + 1),
        Coordinate(coord.get_x() + 1, coord.get_y() - 1),
        Coordinate(coord.get_x() + 1, coord.get_y()),
        Coordinate(coord.get_x() + 1, coord.get_y() + 1)
    ]
    return coords

def get_d_neighbors_9(curve: Curve, coord: Coordinate) -> List[int   ]:
    d = [
        curve.get_d(coord + Coordinate(-1, -1)),
        curve.get_d(coord + Coordinate(-1, 0)),
        curve.get_d(coord + Coordinate(-1, 1)),
        curve.get_d(coord + Coordinate(0, -1)),
        curve.get_d(coord + Coordinate(0, 0)),
        curve.get_d(coord + Coordinate(0, 1)),
        curve.get_d(coord + Coordinate(1, -1)),
        curve.get_d(coord + Coordinate(1, 0)),
        curve.get_d(coord + Coordinate(1, 1))
    ]
    return d