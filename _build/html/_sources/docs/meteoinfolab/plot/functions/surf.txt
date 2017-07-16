.. _docs-meteoinfolab-funcitons-plot-surf:


*******************
surf
*******************

.. currentmodule:: mipylib.plotlib.miplot

.. function:: surf(ax)

    creates a three-dimensional surface plot
    
    :param x: (*array_like*) Optional. X coordinate array.
    :param y: (*array_like*) Optional. Y coordinate array.
    :param z: (*array_like*) 2-D z value array.
    :param cmap: (*string*) Color map string.
    :param xyaxis: (*boolean*) Draw x and y axis or not.
    :param zaxis: (*boolean*) Draw z axis or not.
    :param grid: (*boolean*) Draw grid or not.
    :param boxed: (*boolean*) Draw boxed or not.
    :param mesh: (*boolean*) Draw mesh line or not.
    
    :returns: Legend
    
    **Example:**
    
    ::

        x = arange(1, 10, 0.2)
        y = arange(1, 20, 0.4)
        x, y = meshgrid(x, y)
        z = sin(x) + cos(y)

        #Plot
        ls = surf(x, y, z, 20)
        colorbar(ls,shrink=0.8)
        title('Surface 3D plot example')

    .. image:: ../../../../_static/surf_1.png

    ::

        x = linspace(-2, 2, 25)
        y = linspace(-2, 2, 25)
        x, y = meshgrid(x, y)
        z = x * exp(-x ** 2 - y ** 2)

        #Plot
        ls = surf(x, y, z, 20)
        colorbar(ls,shrink=0.8)
        title('Surface 3D plot example')
        
    .. image:: ../../../../_static/surf_2.png