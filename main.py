from src.curve_utils.curve_validator import validate_curve
from src.curve_utils.dimension import Dimension
from src.pseudo_hilbert_curve import PseudoHilbertCurve
from src.curve_utils.curve_generator import generate_curves, save_100_pseudo_hilbert_curves, calculate_distances_100_pseudo_hilbert_curves, validate_100_pseudo_hilbert_curves

# for key, value in calculate_distances_100_pseudo_hilbert_curves().items():
#     print(key, value)

# curve = PseudoHilbertCurve(80, Dimension(40, 2))
# print(validate_curve(curve))

save_100_pseudo_hilbert_curves()

# for curve in validate_100_pseudo_hilbert_curves():
#     print(curve)