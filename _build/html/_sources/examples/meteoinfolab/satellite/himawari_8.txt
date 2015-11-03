.. _examples-meteoinfolab-satellite-himawari_8:

*******************
Himawari-8 data
*******************

This example code illustrates how to access and visualize a Himawari-8 data. It's very 
hight resolution data with 22000 and 22000 of x and y dimensions, so the step is set to 
4 to reduce the memory usage.

::

    #Add data file
    fn = 'D:/Temp/nc/IDE00220.201507140300.nc'
    f = addfile(fn)
    #Get data variable
    v = f['channel_0003_brf']
    data = v[0,::4,::4]
    data = data[::-1,:]
    #Plot
    ax, proj = axesm(proj='geos', lon_0=104.7, h=35785863, gridlabel=True, gridline=True, frameon=False)
    mlayer = shaperead('D:/Temp/map/country1.shp')
    geoshow(mlayer)
    levs = arange(0, 1, 0.1)
    layer = imshowm(data, levs, proj=proj)
    colorbar(layer)
    
.. image:: image/himawari_8.png