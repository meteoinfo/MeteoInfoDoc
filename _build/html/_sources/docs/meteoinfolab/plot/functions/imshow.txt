.. _docs-meteoinfolab-funcitons-plot-imshow:


*******************
imshow
*******************

.. currentmodule:: mipylib.plotlib.miplot

.. function:: imshow(*args, **kwargs)

    Display an image on the axes.
    
    :param X: (*array_like*) 2-D or 3-D (RGB or RGBA) image value array or BufferedImage.
    :param levs: (*array_like*) Optional. A list of floating point numbers indicating the level curves 
        to draw, in increasing order.
    :param cmap: (*string*) Color map string.
    :param colors: (*list*) If None (default), the colormap specified by cmap will be used. If a 
        string, like ‘r’ or ‘red’, all levels will be plotted in this color. If a tuple of matplotlib 
        color args (string, float, rgb, etc), different levels will be plotted in different colors in 
        the order specified.
    
    :returns: (*Image graphic*) Image graphic created from array data.
    
    **Example:**
    
    ::

        f = addfile('D:/Temp/nc/cone.nc')
        u = f['u'][4,:,:]
        layer = imshow(u, 20)
        title('Cone amplitude - imshow')
        colorbar(layer)
        
    .. image:: ../../../../_static/imshow.png