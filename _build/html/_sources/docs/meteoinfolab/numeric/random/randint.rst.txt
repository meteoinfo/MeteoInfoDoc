.. _docs-meteoinfolab-numeric-random-randint:


**********
randint
**********

.. currentmodule:: numeric.random

.. function:: randint(low, high=None, size=None)

    Return random integers from low (inclusive) to high (exclusive).
    
    Return random integers from the “discrete uniform” distribution of the specified dtype in the “half-open” 
    interval [low, high). If high is None (the default), then results are from [0, low).
    
    :param low: (*int*) Lowest (signed) integer to be drawn from the distribution (unless high=None, in which 
        case this parameter is one above the highest such integer).
    :param high: (*int*) If provided, one above the largest (signed) integer to be drawn from the distribution 
        (see above for behavior if high=None).
    :param size: (*int or tuple*) Output shape. If the given shape is, e.g., (m, n, k), then m * n * k samples 
        are drawn. Default is None, in which case a single value is returned.
        
    :returns: (*int or array*) Random integer array.
    
    Examples::
    
        >>> random.randint(2, size=10)
        array([0, 1, 0, 1, 0, 0, 0, 0, 1, 0])
