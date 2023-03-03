from matplotlib import pyplot as plt
from typing import List, Callable

from src.curve import Curve
from src.curve_utils.plot_utils import plot_curve
from src.curve_utils.dimension import Dimension
from src.pseudo_hilbert_curve import PseudoHilbertCurve


def save_image_curve(curve: Curve, filename: str):
    '''
    Salva curva em um arquivo de imagem .png
    curve: curva a ser plotada
    filename: nome do arquivo da imagem a ser gerada
    '''
    fig, ax = plt.subplots()
    ax.add_collection(plot_curve(curve))
    fig.savefig(filename + '.png')


def generate_curves(curve_type: Callable[[int, Dimension], Curve], dimensions: List[Dimension]) -> List[Curve]:
    '''
    Gera curvas com base nas dimensões passadas
    curve: tipo de curva a ser gerada
    dimensions: dimensões das curvas a serem geradas
    '''
    curves = []
    for dimension in dimensions:
        curve = curve_type(dimension.x * dimension.y, dimension)
        curves.append(curve)
    return curves


def save_100_pseudo_hilbert_curves():
    '''
    Salva imagens de curvas com dimensões de 1x1 à 10x10
    '''
    dimensions = []
    for i in range(1, 11):
        for j in range(1, 11):
            dimensions.append(Dimension(i, j))
    curves = generate_curves(PseudoHilbertCurve, dimensions)
    for curve in curves:
        save_image_curve(curve, f'./plots/pseudohilbert_curve({curve.get_dimension().x}x{curve.get_dimension().y})')


