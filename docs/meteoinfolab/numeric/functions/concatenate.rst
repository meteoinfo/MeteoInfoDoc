.. _docs-meteoinfolab-numeric-funcitons-concatenate:


*******************
concatenate
*******************

.. currentmodule:: mipylib.numeric.minum

.. function:: concatenate(arrays, axis=0)

    Join a sequence of arrays along an existing axis.
    
    :param arrays: (list of arrays) The arrays must have the same shape, except in the dimension 
        corresponding to axis (the first, by default).
    :param axis: (*int*) The axis along which the arrays will be joined. Default is 0.
    
    :returns: (*array_like*) The concatenated array.
    
    Examples::
    
        >>> a = array([[1, 2], [3, 4]])
        >>> b = array([[5, 6]])
        >>> concatenate((a, b), axis=0)
        array([[1, 2],
               [3, 4],
               [5, 6]])
        >>> concatenate((a, b.T), axis=1)
        array([[1, 2, 5],
               [3, 4, 6]])