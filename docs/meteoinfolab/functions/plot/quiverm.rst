.. _docs-meteoinfolab-funcitons-plot-quiverm:


*******************
quiverm
*******************

.. function:: quiverm(*args, **kwargs)

    Plot a 2-D field of arrows in a map.
    
    :param x: (*array_like*) Optional. X coordinate array.
    :param y: (*array_like*) Optional. Y coordinate array.
    :param u: (*array_like*) U component of the arrow vectors (wind field) or wind direction.
    :param v: (*array_like*) V component of the arrow vectors (wind field) or wind speed.
    :param z: (*array_like*) Optional, 2-D z value array.
    :param cmap: (*string*) Color map string.
    :param fill_value: (*float*) Fill_value. Default is ``-9999.0``.
    :param isuv: (*boolean*) Is U/V or direction/speed data array pairs. Default is True.
    :param size: (*float*) Base size of the arrows.
    :param proj: (*ProjectionInfo*) Map projection of the data. Default is None.
    :param order: (*int*) Z-order of created layer for display.
    
    :returns: (*VectoryLayer*) Created quiver VectoryLayer.
    
    **Example:**
    
    ::

        f = addfile('D:/Temp/GrADS/model.ctl')
        u = f['U'][0,'500','10:60','60:140']
        v = f['V'][0,'500','10:60','60:140']
        speed = sqrt(u*u+v*v)
        #Plot
        axesm()
        lworld = shaperead('D:/Temp/Map/country1.shp')
        geoshow(lworld)
        layer = quiverm(u, v, speed, 10, size=8)
        quiverkey(layer, 0.74, 0.18, 15, bbox={'edge':True, 'fill':True})
        colorbar(layer)
        title('Wind field')
        yticks([20,40,60])
        
    .. image:: ../../../../_static/vector.png