.. _docs-meteoinfolab-funcitons-plot-imshowm:


*******************
imshowm
*******************

.. function:: imshowm(*args, **kwargs)

    Display an image on the map.
    
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
    
    :returns: (*RasterLayer*) RasterLayer created from array data.
    
    **Example:**
    
    ::

        #Add data file
        folder = 'D:/Temp/hdf/'
        fns = 'OMI-Aura_L3-OMTO3e_2005m1214_v002-2006m0929t143855.he5'
        fn = folder + fns
        f = addfile(fn)
        vname = 'ColumnAmountO3'
        v = f[vname]
        data = v[:,:]
        #Plot
        axesm()
        mlayer = shaperead('D:/Temp/map/country1.shp')
        geoshow(mlayer, edgecolor='k')
        layer = imshowm(data, 20)
        colorbar(layer)
        title('OMI - ' + vname)
        axism()
        
    .. image:: ../../../../_static/omi_grid.png