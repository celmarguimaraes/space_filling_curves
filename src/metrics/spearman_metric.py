from typing import List
from ..curve import Curve
from itertools import permutations


def calc_covariance(x: List, y: List):
    n = len(x)
    x_mean = sum(x) / n
    y_mean = sum(y) / n
    return sum([(x[i] - x_mean) * (y[i] - y_mean) for i in range(n)]) / n


def calc_stdev(x: List):
    n = len(x)
    x_mean = sum(x) / n
    return (sum([(x[i] - x_mean) ** 2 for i in range(n)]) / n) ** 0.5


def calc_spearman_coefficient(x: List, y: List):
    return calc_covariance(x, y) / (calc_stdev(x) * calc_stdev(y))


def spearman_metric(curve: Curve):
    distances_line = []
    distances_curve = []
    elements_perm = permutations(range(curve.get_number_of_elements()), 2)
    for i, j in elements_perm:
        distances_line.append(abs(i - j))
        distances_curve.append(curve.get_coordinate(i).calculate_distance(curve.get_coordinate(j)))
    return calc_spearman_coefficient(distances_line, distances_curve)

