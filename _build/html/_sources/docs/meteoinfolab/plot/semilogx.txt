.. _docs-meteoinfolab-funcitons-plot-semilogx:


*******************
semilogx
*******************

.. function:: semilogx(*args, **kwargs)

    Make a plot with log scaling on x axis.
    
    :param x: (*array_like*) Input x data.
    :param y: (*array_like*) Input y data.
    :param style: (*string*) Line style for plot.
    
    :returns: Legend breaks of the lines.
      
    Examples::

        t = arange(0.01, 20.0, 0.01)
        semilogx(t, sin(2*pi*t))
        grid(True)
        ylabel('Y Axis')
        xlabel('X Axis')
        legend()
        set(plt.gca, xminortick=True, yminortick=True)
        title('Semilogx')

    .. image:: ../../../../_static/semilogx.png