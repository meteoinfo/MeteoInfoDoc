.. _docs-meteoinfolab-funcitons-plot-loglog:


*******************
loglog
*******************

.. currentmodule:: mipylib.plotlib.miplot

.. function:: loglog(*args, **kwargs)

    Make a plot with log scaling on both x and y axis.
    
    :param x: (*array_like*) Input x data.
    :param y: (*array_like*) Input y data.
    :param style: (*string*) Line style for plot.
    
    :returns: Legend breaks of the lines.
      
    Examples::

        x = [1,3,10]
        y = [1,9,100]
        loglog(x, y, 'r-o')
        ylabel('Y Axis')
        xlabel('X Axis')
        xlim(1e-1, 1e2)
        ylim(1e-1, 1e3)
        legend()
        set(plt.gca, xminortick=True, yminortick=True)
        title('loglog')

    .. image:: ../../../../_static/loglog.png