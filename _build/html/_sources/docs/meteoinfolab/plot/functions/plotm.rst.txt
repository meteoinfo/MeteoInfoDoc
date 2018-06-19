.. _docs-meteoinfolab-funcitons-plot-plotm:


*******************
plotm
*******************

.. currentmodule:: mipylib.plotlib.miplot

.. function:: plotm(*args, **kwargs)

    Plot lines and/or markers to the map.
    
    :param x: (*array_like*) Input x data.
    :param y: (*array_like*) Input y data.
    :param style: (*string*) Line style for plot.
    :param linewidth: (*float*) Line width.
    :param color: (*Color*) Line color.
    
    :returns: (*VectoryLayer*) Line VectoryLayer.     
      
    **Examples**
    
    ::
    
        f = addfile('D:/Temp/hdf/2010128055614_21420_CS_2B-GEOPROF_GRANULE_P_R04_E03.hdf')
        lon = f['Longitude'][:]
        lat = f['Latitude'][:]
        axesm()
        lworld = shaperead('D:/Temp/map/country1.shp')
        geoshow(lworld, edgecolor='k')
        plotm(lon, lat, '-b', linewidth=4)
        scatterm(lon[0], lat[0], size=6, facecolor='r')
        xlim(-180, 180)
        ylim(-90, 90)
        title('Trajectory of Flight Path (starting point in red)')
        
    .. image:: ../../../../_static/plotm.png