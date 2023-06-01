from ..curve import Curve
from ..curve_utils.coordinate import Coordinate
from typing import List
from .metrics_utils import get_coord_neighbors
from math import sqrt


# def average_nearest_neighbor_stretch(curve: Curve, coord: Coordinate):
#     neighbors = get_coord_neighbors(curve, coord)
#     distances = [abs(curve.get_d(coord) - curve.get_d(neighbor)) for neighbor in neighbors]
#     return sum(distances) / len(distances)

def average_nearest_neighbor_stretch(curve: Curve, coord: Coordinate):
    neighbors = get_coord_neighbors(curve, coord)
    distances = [(curve.get_d(coord) - curve.get_d(neighbor)) ** 2 for neighbor in neighbors]
    return sum(distances) / len(distances)

def avg_anns(curve: Curve):
    "Quanto menor melhor"
    return sum([average_nearest_neighbor_stretch(curve, curve.get_coordinate(i)) for i in range(curve.get_number_of_elements())]) / curve.get_number_of_elements()
