.. _docs-meteoinfolab-numeric-funcitons-tile:


*******************
tile
*******************

.. currentmodule:: mipylib.numeric.minum

.. function:: tile(a, repeats)

    Construct an array by repeating ``a`` the number of times given by repeats.
    
    If repeats has length ``d``, the result will have dimension of ``max(d, a.ndim)``.
    
    :param repeats: (*int or list of ints*) The number of repetitions of ``a`` along each 
        axis.
    
    :returns: (*array_like*) Tiled array.
    
    Examples::
    
        >>> b = array([[1, 2], [3, 4]])
        >>> tile(b, 2)
        array([[1, 2, 1, 2],
               [3, 4, 3, 4]])
        >>> tile(b, (2, 1))
        array([[1, 2],
               [3, 4],
               [1, 2],
               [3, 4]])