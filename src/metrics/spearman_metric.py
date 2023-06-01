from typing import List

from ..curve_utils.coordinate import Coordinate
from ..curve import Curve
from itertools import permutations
from .metrics_utils import get_coord_neighbors_9, get_d_neighbors_9
from scipy import stats


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
    res = stats.spearmanr(distances_line, distances_curve)
    return res.correlation

def cluster_spearman_metric(curve: Curve):
    count = 0
    spearman = 0
    for i in range(1, curve.get_dimension().x - 1):
        for j in range(1, curve.get_dimension().y - 1):
            d = get_d_neighbors_9(curve, Coordinate(i, j))
            distances_matrix = []
            distances_curve = []
            elements_perm = permutations(d, 2)
            for k, l in elements_perm:
                if k < l:
                    distances_matrix.append(curve.get_coordinate(k).calculate_distance(curve.get_coordinate(l)))
                    distances_curve.append(abs(k - l))
            res = stats.spearmanr(distances_matrix, distances_curve)
            spearman += res.correlation
            count += 1
    return spearman / count
