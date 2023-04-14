from ..curve import Curve
from ..curve_utils.coordinate import Coordinate
from typing import List


def get_neighbors(curve: Curve, coord: Coordinate) -> List[Coordinate]:
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


def average_nearest_neighbor_stretch(curve: Curve, coord: Coordinate):
    neighbors = get_neighbors(curve, coord)
    distances = [abs(curve.get_d(coord) - curve.get_d(neighbor)) for neighbor in neighbors]
    return sum(distances) / len(distances)

def avg_anns(curve: Curve):
    return sum([average_nearest_neighbor_stretch(curve, curve.get_coordinate(i)) for i in range(curve.get_number_of_elements())]) / curve.get_number_of_elements()
