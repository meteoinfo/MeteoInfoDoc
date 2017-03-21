.. _docs-meteoinfolab-numeric-random-poisson:


**********
poisson
**********

.. currentmodule:: numeric.random

.. function:: poisson(lam=1.0, size=None)

    Draw samples from a Poisson distribution.
    
    :param lam: (*float*) Expectation of interval, should be >= 0.
    :param size: (*int or tuple*) Output shape. If the given shape is, e.g., (m, n, k), then m * n * k samples 
        are drawn. Default is None, in which case a single value is returned.
        
    :returns: (*float or array*) Drawn samples from the parameterized Poisson distribution.
    
    Examples::
    
        >>> random.poisson(5, 100)
        array([5, 5, 5, 6, 6, 2, 7, 5, 4, 4, 4, 7, 7, 6, 4, 5, 5, 5, 5, 3, 6, 2, 6, 3, 3, 4, 6, 6, 5, 4, 6, 3, 3, 6, 4, 5, 9, 1, 3, 4, 3, 6, 6, 5, 4, 3, 5, 4, 9, 3, 6, 5, 5, 1, 6, 6, 1, 4, 13, 4, 3, 2, 5, 3, 2, 1, 4, 1, 2, 8, 6, 7, 5, 2, 6, 5, 6, 2, 5, 4, 4, 6, 5, 4, 3, 3, 4, 3, 4, 12, 9, 6, 4, 3, 5, 5, 4, 8, 4, 8])

