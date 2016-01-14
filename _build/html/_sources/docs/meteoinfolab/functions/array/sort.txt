.. _docs-meteoinfolab-funcitons-array-sort:


*******************
sort
*******************

.. function:: sort(a, axis=-1)

    Return a sorted copy of an array.
    
    :param a: (*array_like*) Array to be sorted.
    :param axis: (*int or None*) Optional. Axis along which to sort. If None, the array is
        flattened after sorting. The default is ``-1`` , which sorts along the last axis.
        
    :returns: (*MIArray*) Sorted array.
                    
    **Examples:**
    
    ::
    
        >>> a = array([[1,4],[3,1]])
        >>> sort(a)                # sort along the last axis
        array([[1, 4],
               [1, 3]])
        >>> sort(a, axis=None)     # sort the flattened array
        array([1, 1, 3, 4])
        >>> sort(a, axis=0)        # sort along the first axis
        array([[1, 1],
               [3, 4]])