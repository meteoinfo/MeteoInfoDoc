.. _docs-meteoinfolab-funcitons-plot-semilogy:


*******************
semilogy
*******************

.. function:: semilogy(*args, **kwargs)

    Make a plot with log scaling on y axis.
    
    :param x: (*array_like*) Input x data.
    :param y: (*array_like*) Input y data.
    :param style: (*string*) Line style for plot.
    
    :returns: Legend breaks of the lines.
      
    Examples::

        x = arange(0, 20.1, 1.0)
        y = exp(-x/5.0)
        semilogy(x, y, 'r-o')
        grid(True)
        ylabel('Y Axis')
        xlabel('X Axis')
        legend()
        xlim(0,20)
        set(plt.gca, xminortick=True, yminortick=True)
        title('Semilogy')

    .. image:: ../../../../_static/semilogy.png