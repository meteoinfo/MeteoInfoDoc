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

The sample code to create Himawari-8 true color image from band 1 (blue), 2 (green) and 3 (red).

::

    #Add data file
    fn = r'C:\Temp\himawari8\NC_H08_20170508_0040_r14_FLDK.02701_02601.nc'
    f = addfile(fn)
    #Read data
    bdata = f['albedo_01'][:,:]
    gdata = f['albedo_02'][:,:]
    rdata = f['albedo_03'][:,:]
    bdata[bdata>1] = 1
    gdata[gdata>1] = 1
    rdata[rdata>1] = 1
    #Plot
    axesm()
    mlayer = shaperead('D:/Temp/map/country1.shp')
    geoshow(mlayer, edgecolor='g')
    layer = imshowm([rdata,gdata,bdata])
    #Adjust image
    imfilter.hsb_adjust(layer, h=0, s=0.1, b=0.2)
    title('Himarari 8 true color image example')
    
.. image:: ../../../_static/himawari8_true_color.png