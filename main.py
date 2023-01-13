from src.pseudo_hilbert_curve import PseudoHilbertCurve
from src.snake_curve import SnakeCurve
from src.curve_utils.dimension import Dimension
from src.curve_utils.plot_utils import plot_curve
from matplotlib import pyplot as plt
from src.curve_utils.plot_utils import get_xy_from_curve

# Caso problemático com solução implementada
# width = 7
# height = 3

# Caso problemático sem solução implementada
width = 130
height = 3
dim = Dimension(width, height)
num_el = width * height

curve = PseudoHilbertCurve(num_el, dim, 3, True)

print(curve.map_d_to_xy)
plot_curve(num_el, curve)
plt.show()