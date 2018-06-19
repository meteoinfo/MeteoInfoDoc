.. _docs-meteoinfolab-numeric-funcitons-argmin:


*******************
argmin
*******************

.. currentmodule:: mipylib.numeric.minum

.. function:: argmin(a, axis=None)

    Returns the indices of the minimum values along an axis.
    
    :param a: (*array_like*) Input array.
    :param axis: (*int*) By default, the index is into the flattened array, otherwise 
        along the specified axis.
        
    :returns: Array of indices into the array. It has the same shape as a.shape with the 
        dimension along axis removed.
    
    Examples::
    
        >>> a = arange(6).reshape(2,3)
        >>> a
        array([[0, 1, 2]
              [3, 4, 5]])
        >>> argmin(a)
        0
        >>> argmin(a, axis=0)
        array([0, 0, 0])
        >>> argmin(a, axis=1)
        array([0, 0])