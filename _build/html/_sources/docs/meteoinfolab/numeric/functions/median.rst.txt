.. _docs-meteoinfolab-numeric-funcitons-median:


*******************
median
*******************

.. currentmodule:: mipylib.numeric.minum

.. function:: median(x, axis=None)

    Compute tha median along the specified axis.
    
    :param x: (*array_like or list*) Input values.
    :param axis: (*int*) Axis along which the standard deviation is computed. 
        The default is to compute the standard deviation of the flattened array.
    
    returns: (*array_like*) Median result
    
    Examples
    
    ::
    
        >>> a = array([[10, 7, 4], [3, 2, 1]])
        >>> a
        array([[10, 7, 4]
              [3, 2, 1]])
        >>> median(a)
        3.5
        >>> median(a, axis=0)
        array([6.5, 4.5, 2.5])
        >>> median(a, axis=1)
        array([7.0, 2.0])

