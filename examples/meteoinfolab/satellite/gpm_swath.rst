.. _examples-meteoinfolab-satellite-gpm_swath:

*******************
GPM swath data
*******************

This example code illustrates how to access and visualize a GPM L1C swath data.

::

    #Add data file
    folder = 'D:/Temp/hdf/'
    fns = '1C.F19.SSMIS.XCAL2015-P.20160105-S214106-E232259.009078.V03A.HDF5'
    fn = folder + fns
    f = addfile(fn)
    lon = f['Longitude'][:,:]
    lat = f['Latitude'][:,:]
    vname = 'Tc'
    v_data = f[vname]
    data = v_data[:,:,0]
    data[data<=-9999.9] = nan
    long_name = v_data.attrvalue('LongName')[0]
    units = v_data.attrvalue('Units')[0]
    #Plot
    axesm()
    geoshow('country', edgecolor='k')
    levs = arange(40, 90, 1)
    layer = pcolor(lon, lat, data, 20)
    colorbar(layer, orientation='horizontal', aspect=40, label=units)
    title('{0}{1}'.format(fns, long_name+' (nchannel1=0)'))
    axism()
    
.. image:: ../../../_static/gpm_swath_1.png