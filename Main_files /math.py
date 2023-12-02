
"""
Have to define a class for operations such as precise estimation 
of square roots, finding intersect points of polynomials 

TODO: 
-> estimation of square roots of numbers
-> finding intersect points of polynomials 

"""


class Operations:
    
    """
    
    The optional parameter will be a list of coeficients of a polynomial
    It will be in a descending order of the magnitude of the power

    e.g.

    3x^3+4x-5 -> [3, 0, 4, -5]

    """

    def __init__(self, *args) -> None:
        self.polynomial = args

