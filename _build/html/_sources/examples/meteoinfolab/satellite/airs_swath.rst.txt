.. _examples-meteoinfolab-satellite-airs_swath:

*******************
AIRS Swath data
*******************

This example code illustrates how to access and visualize a GESDISC AIRS swath data.
**pcolor()** command is used to plot 2 dimension longitude and latitude swath data.
Also **scatter()** command can be used to plot swath data as scatter points.

::

    #Add data file
    folder = 'D:/Temp/hdf/'
    fns = 'AIRS.2002.12.31.001.L2.CC_H.v4.0.21.0.G06100185050.hdf'
    fn = folder + fns
    f = addfile(fn)
    lon_v = f['Longitude']
    lat_v = f['Latitude']
    lon = lon_v[:,:]
    lat = lat_v[:,:]
    vname = 'radiances'
    rad_v = f[vname]
    rad = rad_v[:,:,567]
    #Plot
    plot,proj = axesm(proj='stere', lat_0=-90, gridline=True, griddx=30, griddy=30)
    mlayer = shaperead('D:/Temp/map/country1.shp')
    geoshow(mlayer)
    levs = arange(40, 90, 1)
    #layer = scatter(lon, lat, rad, levs, edge=False)
    layer = pcolor(lon, lat, rad, levs)
    colorbar(layer, orientation='horizontal')
    title('{0}\n {1}'.format(fns, vname))
    axism()
    
.. image:: image/airs_swath.png