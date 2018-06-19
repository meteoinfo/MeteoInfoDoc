.. _docs-meteoinfolab-numeric-funcitons-argmax:


*******************
argmax
*******************

.. currentmodule:: mipylib.numeric.minum

.. function:: argmax(a, axis=None)

    Returns the indices of the maximum values along an axis.
    
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
        >>> argmax(a)
        5
        >>> argmax(a, axis=0)
        array([1, 1, 1])
        >>> argmax(a, axis=1)
        array([2, 2])