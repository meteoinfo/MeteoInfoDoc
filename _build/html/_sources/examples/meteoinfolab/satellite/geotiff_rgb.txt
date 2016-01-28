.. _examples-meteoinfolab-satellite-geotiff_rgb:

*******************
GeoTiff RGB image
*******************

This example code illustrates how to plot a GeoTiff RGB image.

::

    f = addfile('D:/Temp/satellite/PI_H08_20151224_0450_TRC_CHN_R10_PGPFD.tif')
    data = f['var'][None]
    axesm()
    lworld = shaperead('D:/Temp/Map/country1.shp')
    lchina = shaperead('D:/Temp/Map/bou2_4p.shp')
    geoshow(lworld, edgecolor=[102,102,255])
    geoshow(lchina, edgecolor=[102,102,255])
    layer = imshowm(data)
    title('Geotiff - RGB')
    
.. image:: ../../../_static/geotiff_rgb.png