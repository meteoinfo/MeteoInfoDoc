.. _docs-meteoinfolab-funcitons-array-reshape:


*******************
reshape
*******************

.. function:: reshape(a, shape)

    Gives a new shape to an array without changing its data.
    
    :param a: (*array_like*) Array to be reshaped.
    :param shape: (*int or tuple of ints*) The new shape should be compatible with the original 
        shape. If an integer, then the result will be a 1-D array of that length. One shape 
        dimension can be -1. In this case, the value is inferred from the length of the array and 
        remaining dimensions.
        
    :returns: Reshaped array.
                    
    Examples
    
    ::
    
        >>> a = array([[1,2,3], [4,5,6]])
        >>> a
        array([[1, 2, 3]
              [4, 5, 6]])
        >>> reshape(a, 6)
        array([1, 2, 3, 4, 5, 6])
        >>> reshape(a, (3, 2))
        array([[1, 2]
              [3, 4]
              [5, 6]])