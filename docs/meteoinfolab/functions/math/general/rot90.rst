.. _docs-meteoinfolab-funcitons-math-rot90:


*******************
rot90
*******************

.. function:: rot90(a, k=1)

    Rotate an array by 90 degrees in the counter-clockwise direction. The first two dimensions
    are rotated if the array has more than 2 dimensions.
    
    :param a: (*array_like*) Array for rotate.
    :param k: (*int*) Number of times the array is rotated by 90 degrees
    
    :returns: (*array_like*) Rotated array.
    
    Examples::
    
        >>> m = array([[1,2],[3,4]])
        >>> m
        >>> array([[1, 2]
              [3, 4]])
        >>> rot90(m)
        array([[2, 4]
              [1, 3]])
        >>> rot90(m, 2)
        array([[4, 3]
              [2, 1]])