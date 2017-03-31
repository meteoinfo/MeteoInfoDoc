.. _docs-meteoinfolab-funcitons-plot-hist:


*******************
hist
*******************

.. currentmodule:: mipylib.plotlib.miplot

.. function:: hist(x, bins=10, **kwargs)

    Plot a histogram.
    
    :param x: (*array_like*) Input values, this takes either a single array or a sequency of arrays 
        which are not required to be of the same length.
    :param bins: (*int*) If an integer is given, bins + 1 bin edges are returned.
    
    Examples:
    
    ::

        x = random.randn(10000)
        hist(x, bins=50, color='c')
        title('Histogram')
        
    .. image:: ../../../../_static/hist_1.png