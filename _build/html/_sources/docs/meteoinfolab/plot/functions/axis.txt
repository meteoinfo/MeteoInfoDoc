.. _docs-meteoinfolab-funcitons-plot-axis:


*******************
axis
*******************

.. currentmodule:: mipylib.plotlib.miplot

.. function:: axis(limits)

    Sets the min and max of the x and y axes, with ``[xmin, xmax, ymin, ymax]`` .
    
    :param limits: (*list*) Min and max of the x and y axes.
    
    **Example:**
    
    ::

        >>> axis([1, 20, 3, 25])