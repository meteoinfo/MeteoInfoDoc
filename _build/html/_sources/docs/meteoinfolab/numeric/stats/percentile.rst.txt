.. _docs-meteoinfolab-numeric-stats-percentile:


**********
percentile
**********

.. currentmodule:: numeric.stats

.. function:: percentile(a, q, axis=None)

    Compute the qth percentile of the data along the specified axis.
    
    :param a: (*array_like*) Input array.
    :param q: (*float*) float in range of [0,100].
        Percentile to compute, which must be between 0 and 100 inclusive.
    :param axis: (*int*) Axis or axes along which the percentiles are computed. The default is 
        to compute the percentile along a flattened version of the array.
    
    :returns: (*float*) qth percentile value.
    
    Examples::
    
        >>> a = array([[10, 7, 4], [3, 2, 1]])
        >>> a
        array([[10, 7, 4]
              [3, 2, 1]])
        >>> percentile(a, 50)
        3.5
        >>> percentile(a, 50, axis=0)
        array([6.5, 4.5, 2.5])
        >>> percentile(a, 50, axis=1)
        array([7.0, 2.0])