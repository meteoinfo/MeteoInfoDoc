.. _docs-meteoinfolab-funcitons-plot-contourfm:


*******************
contourfm
*******************

.. function:: contourfm(*args, **kwargs)

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
    :param fill_value: (*float*) Fill_value. Default is ``-9999.0``.
    :param proj: (*ProjectionInfo*) Map projection of the data. Default is None.
    :param order: (*int*) Z-order of created layer for display.
    
    :returns: (*VectoryLayer*) Contour filled VectoryLayer created from array data.
    
    **Example:**
    
    ::

        f = addfile('D:/Temp/GrADS/model.ctl')
        psv = f['PS']
        ps = psv[0,[10,60],[60,140]]
        axesm()
        mlayer = shaperead('D:/Temp/map/country1.shp')
        geoshow(mlayer, edgecolor=(0,0,255))
        layer = contourfm(ps, 20)
        cl = contourm(ps, 20, colors='gray')
        clabel(cl)
        title('Pressure')
        yticks(arange(20, 61, 20))
        grid()
        colorbar(layer, orientation='horizontal', extendrect=False, shrink=0.8, aspect=12)
        
    .. image:: ../../../../_static/contourm_1.png