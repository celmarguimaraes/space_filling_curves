import math
from src.curve import Curve
from src.curve_utils.dimension import Dimension
from src.curve_utils.coordinate import Coordinate
from zCurve import zCurve
from math import sqrt

class MortonCurve(Curve):
    def __init__(self, num_of_elements: int, dimension:Dimension) -> None:
        super().__init__(num_of_elements, dimension)


    def get_d(self, coordinate:Coordinate) -> int:
        return zCurve.interlace(coordinate.get_x(), coordinate.get_y(), dims=2)
        

    def get_coordinate(self, d:int) -> Coordinate:
        d = zCurve.deinterlace(d, dims=2, total_bits=sqrt(self.number_of_elements))
        return Coordinate(d[0], d[1])


    def define_dimension(self, number_of_elements:int) -> Dimension:
       d = math.ceil(math.sqrt(number_of_elements))
       return Dimension(d, d)