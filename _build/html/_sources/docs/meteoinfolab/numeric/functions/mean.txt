.. _docs-meteoinfolab-numeric-funcitons-mean:


*******************
mean
*******************

.. currentmodule:: mipylib.numeric.minum

.. function:: mean(x, axis=None)

    Compute tha arithmetic mean along the specified axis.
    
    :param x: (*array_like or list*) Input values.
    :param axis: (*int*) Axis along which the standard deviation is computed. 
        The default is to compute the standard deviation of the flattened array.
    
    returns: (*array_like*) Mean result
    
    Examples
    
    ::
    
        >>> a = array([[1, 2], [3, 4]])
        >>> mean(a)
        2.5
        >>> mean(a, axis=0)
        array([2.0, 3.0])
        >>> mean(a, axis=1)
        array([1.5, 3.5])
