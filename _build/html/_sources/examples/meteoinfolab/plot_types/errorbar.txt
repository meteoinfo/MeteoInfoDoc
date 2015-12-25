.. _examples-meteoinfolab-plot_types-errorbar:

*******************
Errorbar chart
*******************

Errorbar chart was created by ``errorbar()`` function.

Fixed x, y error values:

::

    x = arange(0.1, 4, 0.5)
    y = exp(-x)
    errorbar(x, y, fmt='b', xerr=0.2, yerr=0.4)
    title('Fixed error values example')
    
.. image:: ../../../_static/errorbar_1.png

Variable y error values.

::

    x = arange(0.1, 4, 0.5)
    y = exp(-x)
    # example error bar values that vary with x-position
    error = 0.1 + 0.2 * x
    errorbar(x, y, yerr=error, fmt='b-o')
    title('Variable error bar values example')
    
.. image:: ../../../_static/errorbar_2.png