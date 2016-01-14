.. _docs-meteoinfolab-funcitons-plot-scatterm:


*******************
scatterm
*******************

.. function:: scatterm(*args, **kwargs)

    Make a scatter plot on a map.
    
    :param x: (*array_like*) Input x data.
    :param y: (*array_like*) Input y data.
    :param z: (*array_like*) Input z data.
    :param levs: (*array_like*) Optional. A list of floating point numbers indicating the level curves 
        to draw, in increasing order.
    :param cmap: (*string*) Color map string.
    :param colors: (*list*) If None (default), the colormap specified by cmap will be used. If a 
        string, like ‘r’ or ‘red’, all levels will be plotted in this color. If a tuple of matplotlib 
        color args (string, float, rgb, etc), different levels will be plotted in different colors in 
        the order specified.
    :param size: (*int*) Marker size.
    :param marker: (*string*) Marker of the points.
    :param fill: (*boolean*) Fill markers or not. Default is True.
    :param edge: (*boolean*) Draw edge of markers or not. Default is True.
    :param facecolor: (*Color*) Fill color of markers. Default is black.
    :param edgecolor: (*Color*) Edge color of markers. Default is black.
    :param fill_value: (*float*) Fill_value. Default is ``-9999.0``.
    :param proj: (*ProjectionInfo*) Map projection of the data. Default is None.
    :param order: (*int*) Z-order of created layer for display.
    
    :returns: (*VectoryLayer*) Point VectoryLayer.
      
    Examples::

        f = addfile_micaps('D:/Temp/micaps/10101414.000')
        vname = 'Precipitation6h'
        pr = f[vname][:]
        lon = f['Longitude'][:]
        lat = f['Latitude'][:]
        layer = shaperead('D:/Temp/map/china.shp')
        pr, lon, lat = rmaskout(pr, lon, lat, layer.shapes())
        axesm()
        mlayer = shaperead('D:/Temp/map/country1.shp')
        geoshow(mlayer, edgecolor=(0,0,255))
        levs = [0.1, 1, 2, 5, 10, 20, 25, 50, 100]
        cols = [(255,255,255),(170,240,255),(120,230,240),(200,220,50),(240,220,20),(255,120,10),(255,90,10), \
            (240,40,0),(180,10,0),(120,10,0)]
        layer = scatterm(lon, lat, pr, levs, colors = cols, s=2, edgecolor='gray')
        title(vname)
        yticks(arange(20, 51, 10))
        xlim(70, 140)
        ylim(15, 55)
        colorbar(layer, orientation='horizontal', shrink=0.8, aspect=30)
        
    .. image:: ../../../../_static/scatterm.png