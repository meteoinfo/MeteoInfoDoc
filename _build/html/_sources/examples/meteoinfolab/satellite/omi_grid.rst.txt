.. _examples-meteoinfolab-satellite-omi_grid:

*******************
OMI grid data
*******************

This example code illustrates how to access and visualize a OMI grid data.

::

    #Add data file
    folder = 'D:/Temp/hdf/'
    fns = 'OMI-Aura_L3-OMTO3e_2005m1214_v002-2006m0929t143855.he5'
    fn = folder + fns
    f = addfile(fn)
    vname = 'ColumnAmountO3'
    v = f[vname]
    data = v[:,:]
    #Plot
    axesm()
    mlayer = shaperead('D:/Temp/map/country1.shp')
    geoshow(mlayer, edgecolor='k')
    layer = imshowm(data, 20)
    colorbar(layer)
    title('OMI - ' + vname)
    axism()
    
.. image:: ../../../_static/omi_grid.png