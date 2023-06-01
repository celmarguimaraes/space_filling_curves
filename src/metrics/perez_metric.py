from ..curve_utils.coordinate import Coordinate
from ..curve import Curve
import matplotlib.pyplot as plt


def perez_metric(curve: Curve):
    perez_sum = 0
    for i in range(curve.number_of_elements):
        for j in range(i + 1, curve.number_of_elements):
            try:
                "Quanto maior o denominador que representa a distância na matriz, menor o resultado, ou seja, pior é a situação da curva"
                "Denominador grande, a distância na matriz é muito grande comparada com a distância na curva. 2 pontos são vizinhos na curva, mas a distância na matriz é muito grande."
                perez_sum += abs(i - j)/Coordinate.calculate_distance(curve.get_coordinate(i), curve.get_coordinate(j))
            except:
                perez_sum += 0
    return perez_sum


def perez_mean(curve: Curve):
    "Quanto mais próximo de 1, melhor a situação da curva"
    return perez_metric(curve) / ((curve.number_of_elements * (curve.number_of_elements - 1)) / 2)


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

