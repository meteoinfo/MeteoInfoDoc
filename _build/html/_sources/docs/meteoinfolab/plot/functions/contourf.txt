.. _docs-meteoinfolab-funcitons-plot-contourf:


*******************
contourf
*******************

.. currentmodule:: mipylib.plotlib.miplot

.. function:: contourf(*args, **kwargs)

    Plot filled contours.
    
    :param x: (*array_like*) Optional. X coordinate array.
    :param y: (*array_like*) Optional. Y coordinate array.
    :param z: (*array_like*) 2-D z value array.
    :param levs: (*array_like*) Optional. A list of floating point numbers indicating the level curves 
        to draw, in increasing order.
    :param cmap: (*string*) Color map string.
    :param colors: (*list*) If None (default), the colormap specified by cmap will be used. If a 
        string, like ‘r’ or ‘red’, all levels will be plotted in this color. If a tuple of matplotlib 
        color args (string, float, rgb, etc), different levels will be plotted in different colors in 
        the order specified.
    
    :returns: (*VectoryLayer*) Contour filled VectoryLayer created from array data.
    
    **Example:**
    
    ::

        f = addfile('D:/Temp/nc/cone.nc')
        u = f['u'][4,:,:]
        subplot(2,1,1)
        layer = contour(u)
        clabel(layer)
        title('Cone amplitude')
        colorbar(layer)

        subplot(2,1,2)
        u = f['u'][5,:,:]
        layer = contourf(u)
        title('Cone amplitude')
        colorbar(layer)
        
    .. image:: ../../../../_static/contour.png