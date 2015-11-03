.. _docs-meteoinfolab-funcitons-array-arange:


*******************
arange
*******************

.. function:: arange([start, ]stop, [step, ]dtype=None)

    Return evenly spaced values within a given interval
    
    Values are generated within the half-open interval ``[start, stop]`` (in other words,
    the interval including *start* but excluding *stop*).
    
    When using a non-integer step, such as 0.1, the results will often not be consistent.
    It is better to use ``linespace`` for these cases.
    
    :param start: (*number, optional*) Start of interval. The interval includes this value.
        The default start value is 0.
    :param stop: (*number*) End of interval. The interval does not include this value,
        except in some cases where *step* is not an integer and floating point round-off
        affects the length of *out*.
    :param step: (*number, optional*) Spacing between values. For any output *out*, this
        is the distance between two adjacent values, ``out[i+1] - out[i]``. The default
        step size is 1. If *step* is specified. *start* must also be given.
    :param dtype: (*dtype*) The type of output array. If dtype is not given, infer the data
        type from the other input arguments.
        
    :returns: (*MIArray*) Array of evenly spaced values.
    
    Examples
    
    ::
    
        >>> arange(3)
        array([0, 1, 2])
        >>> arange(3,7,2)
        array([3, 5])