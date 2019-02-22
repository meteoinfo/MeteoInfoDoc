.. _examples-meteoinfolab-satellite-smap_l4:

*******************
SMAP L4 data
*******************

This example code illustrates how to access and visualize a SMAP L4 data.

::

    #Add data file
    print 'Read data...'
    fn = 'D:/Temp/hdf/SMAP_L4_SM_gph_20150414T013000_Vb1010_001.h5'
    f = addfile(fn)
    lon = f['cell_lon'][:,:]
    lat = f['cell_lat'][::-1,:]
    #vname = 'surface_temp'
    #vname = 'sm_surface_wetness'
    #vname = 'sm_surface'
    vname = 'sm_profile'
    v = f[vname]
    data = v[::-1,:]
    longname = v.attrvalue('long_name')[0]
    units = v.attrvalue('units')[0]

    #Interpolate data to grid
    print 'Interpolate data to grid...'
    lon1 = linspace(lon.min(), lon.max(), lon.dimlen(1))
    lat1 = linspace(lat.min(), lat.max(), lat.dimlen(0))
    data1 = griddata((lon, lat), data, xi=(lon1, lat1), method='surface')[0]

    #Plot
    print 'Plot...'
    axesm()
    geoshow('country', edgecolor='k')
    layer = imshowm(lon1, lat1, data1, 20, cmap='wcgyr_1000', interpolation='bilinear')
    colorbar(layer, label=units)
    title('{0}\n {1}'.format(fn, longname))
    print 'Finish!'
    
.. image:: ../../../_static/smap_l4.png