.. _examples-meteoinfolab-satellite-mod10a1_snow:

*******************
MODIS snow data - MOD10A1
*******************

This example code illustrates how to access and visualize a MODIS snow albedo (MOD10A1)
data. The MODIS land products are produced and distributed in adjacent non-overlapping
tiles that are approximately 10 degrees square (at the equator). Most of the higher
resolution MODIS land products are produced in the Sinusoidal tile grid.

::

    f = addfile('D:/Temp/Hdf/MOD10A1.A2010365.h27v05.005.2011002103013.hdf')
    vname = 'snow_Albedo_Daily_Tile'
    data = f[vname][:,:]
    axesm(projinfo=f.proj, griddx=30, griddy=30, gridline=True)
    #axesm(griddx=30, griddy=30, gridline=True)
    mlayer = shaperead('D:/Temp/map/country1.shp')
    geoshow(mlayer, edgecolor='k')
    levs = arange(0, 100, 5)
    layer = imshowm(data, 20, proj=f.proj)
    title(vname)
    colorbar(layer)
    axism()
    
.. image:: image/mod10a1_snow.png

Zoom to data tile extent:

.. image:: image/mod10a1_snow_zoom.png