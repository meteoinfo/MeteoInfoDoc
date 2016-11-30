.. _docs-meteoinfolab-funcitons-array-logspace:


*******************
logspace
*******************

.. function:: logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)

    Return numbers spaced evenly on a log scale.

    In linear space, the sequence starts at base ** start (*base to the power of start*) and ends with
    base ** stop.
    
    :param start: (*float*) Base ** start is the starting value of the sequence.
    :param stop: (*float*) Base ** stop is the final value of the sequence, unless *endpoint* is False.
        In that case, num + 1 values are spaced over the interval in log-space, of which all but the last
        (a sequence of length num) are returned.
    :param num: (*int, optional*) Number of samples to generate. Default is 50. Must 
        be non-negative.
    :param base: (*float, optional*) The base of the log space. The step size between the elements in
        ln(samples) / ln(base) (or log_base(samples)) is uniform. Default is 10.0. 
    :param endpoint: (*boolean, optional*) If true, stop is the last sample. Otherwise, it is not included. 
        Default is True.
    :param dtype: (*dtype*) The type of output array. If dtype is not given, infer the data
        type from the other input arguments.
        
    :returns: (*MIArray*) Array of evenly spaced values.
    
    Examples::
    
        >>> logspace(2.0, 3.0, num=4)
        array([100.0, 215.4434295785405, 464.1589682991224, 1000.0])
        >>> logspace(2.0, 3.0, num=4, base=2.0)
        array([4.0, 5.0396839219614975, 6.349604557649573, 8.0])