.. _docs-meteoinfolab-numeric-funcitons-sum:


*******************
sum
*******************

.. currentmodule:: mipylib.numeric.minum

.. function:: sum(x, axis=None)

    Sum of array elements over a given axis.
    
    :param x: (*array_like or list*) Input values.
    :param axis: (*int*) Axis along which the standard deviation is computed. 
        The default is to compute the standard deviation of the flattened array.
    
    returns: (*array_like*) Sum result
    
    Examples
    
    ::
    
        >>> a = array([[0, 1], [0, 5]])
        >>> sum(a)
        6.0
        >>> sum(a, axis=0)
        array([0.0, 6.0])
        >>> sum(a, axis=1)
        array([1.0, 5.0])
