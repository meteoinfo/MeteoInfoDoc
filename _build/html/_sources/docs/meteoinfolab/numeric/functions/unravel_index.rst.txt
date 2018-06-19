.. _docs-meteoinfolab-numeric-funcitons-unravel_index:


*******************
unravel_index
*******************

.. currentmodule:: mipylib.numeric.minum

.. function:: unravel_index(a, dims)

    Converts a flat index or array of flat indices into a tuple of coordinate arrays.
    
    :param indices: (*array_like*) An integer array whose elements are indices into the 
        flattened version of an array of dimensions ``dims``.
    :param dims: (*tuple of ints*) The shape of the array to use for unraveling indices.
    
    :returns: tuple of ndarray. Each array in the tuple has the same shape as the indices 
        array.
    
    Examples::
    
        >>> unravel_index(22, (7,6))
        (3, 4)