# Métrica 1: quantidade de elementos vizinhos na curva que também são vizinhos na matriz
# Ideia: percorrer curva e verificar se vizinhos na reta são vizinhos na matriz.

# Métrica 2: quantidade de elementos vizinhos na matriz que também são vizinhos na curva
# Ideia: 
#   Passo 1: passar por todos os pares de células vizinhas nas colunas da matriz e verificar se são vizinhos na curva.
#   Passo 2: passar por todos os pares de células vizinhas nas linhas da matriz e verificar se são vizinhos na curva.

from ..curve import Curve
from .metrics_utils import get_coord_neighbors, is_coord_neighbor, get_d_neighbors


def metric_neighbor_from_curve(curve: Curve) -> float:
    count = 0
    for i in range(curve.get_number_of_elements()):
        neighbors = get_coord_neighbors(
            curve, 
            curve.get_coordinate(i)
        )
        for neighbor in neighbors:
            if (
                curve.get_d(neighbor) == i - 1 
                or curve.get_d(neighbor) == i + 1
            ):
                count += 1
    return count



def metric_neighbor_from_d(curve: Curve) -> float:
    count = 0
    for i in range(curve.get_number_of_elements()):
        neighbors = get_d_neighbors(curve, i)
        for neighbor in neighbors:
            if is_coord_neighbor(
                curve.get_coordinate(neighbor), 
                curve.get_coordinate(i)
            ):
                count += 1
    return count
