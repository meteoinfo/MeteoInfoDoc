.. _docs-meteoinfolab-funcitons-array-linspace:


*******************
linspace
*******************

.. function:: linspace(start, stop, num=50, endpoint=True, dtype=None)

    Return evenly spaced numbers over a specified interval.

    Returns *num* evenly spaced samples, calculated over the interval [*start, stop*].

    The endpoint of the interval can optionally be excluded.
    
    :param start: (*number*) Start of interval. The interval includes this value.
    :param stop: (*number*) The end value of the sequence, unless endpoint is set to 
        False. In that case, the sequence consists of all but the last of ``num + 1`` 
        evenly spaced samples, so that stop is excluded. Note that the step size changes 
        when endpoint is False.
    :param num: (*number, optional*) Number of samples to generate. Default is 50. Must 
        be non-negative.
    :param dtype: (*dtype*) The type of output array. If dtype is not given, infer the data
        type from the other input arguments.
        
    :returns: (*MIArray*) Array of evenly spaced values.
    
    Examples
    
    ::
    
        >>> linspace(2.0, 3.0, num=5)
        array([2.0, 2.25, 2.5, 2.75, 3.0])
        >>> linspace(2.0, 3.0, num=5, endpoint=False)
        array([2.0, 2.25, 2.5, 2.75])