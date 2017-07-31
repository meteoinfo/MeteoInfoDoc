.. _docs-meteoinfolab-numeric-funcitons-std:


*******************
std
*******************

.. currentmodule:: mipylib.numeric.minum

.. function:: std(x, axis=None)

    Compute the standard deviation along the specified axis.
    
    :param x: (*array_like or list*) Input values.
    :param axis: (*int*) Axis along which the standard deviation is computed. 
        The default is to compute the standard deviation of the flattened array.
    
    returns: (*array_like*) Standart deviation result.
    
    Examples
    
    ::
    
        >>> a = array([[1, 2], [3, 4]])
        >>> std(a)
        1.118033988749895
        >>> std(a, axis=0)
        array([1.0, 1.0])
        >>> std(a, axis=1)
        array([0.5, 0.5])