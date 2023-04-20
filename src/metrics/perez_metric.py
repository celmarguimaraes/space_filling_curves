from ..curve_utils.coordinate import Coordinate
from ..curve import Curve
import matplotlib.pyplot as plt


def perez_metric(curve: Curve):
    perez_sum = 0
    for i in range(curve.number_of_elements):
        for j in range(i + 1, curve.number_of_elements):
            try:
                perez_sum += abs(i - j)/Coordinate.calculate_distance(curve.get_coordinate(i), curve.get_coordinate(j))
            except:
                perez_sum += 0
    return perez_sum


def perez_matrix(curve: Curve):
    matrix = [[0 for i in range(curve.number_of_elements)] for j in range(curve.number_of_elements)]
    for i in range(curve.number_of_elements):
        for j in range(curve.number_of_elements):
            try:
                c1 = curve.get_coordinate(i)
                c2 = curve.get_coordinate(j)
                perez_coef = round(abs(i - j) / Coordinate.calculate_distance(c1, c2))
                matrix[i][j] = perez_coef
            except:
                matrix[i][j] = 0
    return matrix

