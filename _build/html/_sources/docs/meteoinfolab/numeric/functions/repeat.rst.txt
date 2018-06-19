.. _docs-meteoinfolab-numeric-funcitons-repeat:


*******************
repeat
*******************

.. currentmodule:: mipylib.numeric.minum

.. function:: repeat(a, repeats, axis=None)

    Repeat elements of an array.
    
    :param repeats: (*int or list of ints*) The number of repetitions for each 
        element. repeats is broadcasted to fit the shape of the given axis.
    :param axis: (*int*) The axis along which to repeat values. By default, use 
        the flattened input array, and return a flat output array.
    
    :returns: (*array_like*) Repeated array.
    
    Examples::
    
        >>> repeat(3, 4)
        array([3, 3, 3, 3])
        >>> x = array([[1,2],[3,4]])
        >>> repeat(x, 2)
        array([1, 1, 2, 2, 3, 3, 4, 4])
        >>> repeat(x, 3, axis=1)
        array([[1, 1, 1, 2, 2, 2],
               [3, 3, 3, 4, 4, 4]])
        >>> repeat(x, [1, 2], axis=0)
        array([[1, 2],
               [3, 4],
               [3, 4]])