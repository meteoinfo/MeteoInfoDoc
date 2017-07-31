.. _examples-meteoinfolab-satellite-avhrr_sst:

*******************
AVHRR Grid data
*******************

This example code illustrates how to access and visualize a AVHRR grid data.

::

    #Add data file
    f = addfile('D:/Temp/hdf/2006001-2006005.s0454pfrt-bsst.hdf')
    vname = 'bsst'
    v = f[vname]
    data = v[:,:]
    data.fill_value = 0.0
    #Plot
    axesm()
    geoshow('country')
    layer = imshowm(data, 20)
    colorbar(layer)
    title('AVHRR - ' + vname)
    axism()
    
.. image:: ../../../_static/avhrr_sst.png