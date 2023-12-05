import math.py

"""
The class matrix will contruct the matrix, by first creating the individual columns
and then putting those columns into one matrix

TODO: 
-> Create columns
-> create put the columns into a matrix
-> row operations:
    -> scalar multiplication
    -> row addition 
    -> row swap

"""

class Matrix: 
    

    """
    When creating the matrix the values that need to be inputed are:
    m -> number of rows
    n -> number of columns 
    args -> the values of in the matrix (starting with the first value in the first column 
            and going down the column, column by column)
    """

    def __init__(self, m, n, *args) -> None:
        
        self.rows = m
        self.columns = n
        self.values = args

        