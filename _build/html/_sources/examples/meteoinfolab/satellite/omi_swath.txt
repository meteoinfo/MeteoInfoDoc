.. _examples-meteoinfolab-satellite-omi_swath:

*******************
OMI swath data
*******************

This example code illustrates how to access and visualize a OMI swath data.

::

    #Add data file
    folder = 'D:/Temp/hdf/'
    fns = 'OMI-Aura_L2-OMNO2_2008m0720t2016-o21357_v003-2008m0721t101450.he5'
    fn = folder + fns
    f = addfile(fn)
    lon_v = f['Longitude']
    lat_v = f['Latitude']
    lon = lon_v[:,:]
    lat = lat_v[:,:]
    vname = 'CloudFraction'
    v = f[vname]
    data = v[:,:]*0.001
    #Plot
    axesm()
    mlayer = shaperead('D:/Temp/map/country1.shp')
    geoshow(mlayer, edgecolor='k')
    #slayer = scatterm(lon, lat, data, edge=False)
    layer = surfacem(lon, lat, data)
    colorbar(layer)
    title('OMI - ' + vname)
    axism()
    
.. image:: image/omi_swath.png