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
    lon = f['Longitude'][:]
    lat = f['Latitude'][:]
    vname = 'CloudFraction'
    data = f[vname][:]*0.001

    #Plot
    axesm()
    geoshow('country')
    #slayer = scatter(lon, lat, data, edge=False)
    layer = pcolor(lon, lat, data)
    colorbar(layer)
    title('OMI - ' + vname)
    axism()
    
.. image:: image/omi_swath.png