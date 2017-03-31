.. _docs-meteoinfolab-funcitons-plot-antialias:


*******************
antialias
*******************

.. currentmodule:: mipylib.plotlib.miplot

.. function:: antialias(b=True)

    Set figure antialias or not.
    
    :param b: (*boolean*) Set figure antialias or not. Default is ``False`` .
    
    **Example:**
    
    Before antialias::

        def f(t):
            return exp(-t) * cos(2*pi*t)

        t1 = arange(0., 5., 0.1)
        t2 = arange(0., 5., 0.02)
        plot(t1, f(t1), 'bo', t2, f(t2), 'k')
        plot(t2, cos(2*pi*t2), 'r--')
        title('XY plot')
        xlabel('X axis')
        ylabel('Y axis')
        legend()
        
    .. image:: ../../../../_static/xy_plot.png
    
    After antialias::
    
        >>> antialias()
        
    .. image:: ../../../../_static/xy_plot_antialias.png