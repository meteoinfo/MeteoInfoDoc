.. _docs-meteoinfolab-funcitons-plot-arrow:


*******************
arrow
*******************

.. currentmodule:: mipylib.plotlib.miplot

.. function:: arrow(self, x, y, dx, dy, **kwargs)

    Add an arrow to the axes.
        
    :param x: (*float*) X coordinate.
    :param y: (*float*) Y coordinate.
    :param dx: (*float*) The length of arrow along x direction. 
    :param dy: (*float*) The length of arrow along y direction.
    
    :returns: Arrow graphic.
    
    **Example:**
    
    ::
    
        v = [-0.2, 0, .2, .4, .6, .8, 1]
        for i, overhang in enumerate(v):
            arrow(.1,overhang,.6,0, headwidth=0.05, overhang=overhang, length_includes_head=True)

        xlim(0, 1)
        ylim(-0.3, 1.1)
        yticks(v)
        xticks([])
        ylabel('overhang')
        antialias(True)
        
    .. image:: ../../../../_static/arrow_overhang.png