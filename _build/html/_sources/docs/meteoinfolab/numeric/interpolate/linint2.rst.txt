.. _docs-meteoinfolab-numeric-interpolate-linint2:


*******************
linint2
*******************

.. currentmodule:: mipylib.numeric.interpolate

.. function:: linint2(*args, **kwargs)

    Interpolates from a rectilinear grid to another rectilinear grid using bilinear interpolation.
    
    :param x: (*array_like*) X coordinate array of the sample data (one dimension).
    :param y: (*array_like*) Y coordinate array of the sample data (one dimension).
    :param z: (*array_like*) Value array of the sample data (multi-dimension, last two dimensions are y and x).
    :param xq: (*array_like*) X coordinate array of the query data (one dimension).
    :param yq: (*array_like*) Y coordinate array of the query data (one dimension).
    
    :returns: (*array_like*) Interpolated array.
    
    **Examples**
    
    ::

        fn = os.path.join(migl.get_sample_folder(), 'GrADS', 'model.ctl')
        f = addfile(fn)
        ps = f['PS'][:,'10:60','60:140']
        lon = arange(50, 142, 2.5)
        lat = arange(5, 66, 2.5)
        nps = interpolate.linint2(ps, lon, lat)

        levs = arange(500, 1021, 20)

        #Plot
        subplot(2,1,1,axestype='map')
        geoshow('country', edgecolor=(0,0,255))
        layer = imshow(lon, lat, nps[1,:,:], levs)
        title('Pressure - linint2')
        colorbar(layer)

        subplot(2,1,2,axestype='map')
        geoshow('country', edgecolor=(0,0,255))
        layer = imshow(ps[1,:,:], levs)
        title('Pressure - origin')
        colorbar(layer)
        
.. image:: ../../../../_static/linint2.png