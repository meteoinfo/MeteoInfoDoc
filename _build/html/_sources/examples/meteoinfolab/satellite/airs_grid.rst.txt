.. _examples-meteoinfolab-satellite-airs_grid:

*******************
AIRS Grid data
*******************

This example code illustrates how to access and visualize a GESDISC AIRS grid.

::

    #Add data file
    folder = 'D:/Temp/hdf/'
    fns = 'AIRS.2002.08.01.L3.RetStd_H031.v4.0.21.0.G06104133732.hdf'
    fn = folder + fns
    f = addfile(fn)
    vname = 'Temperature_MW_A'
    t_v = f[vname]
    t = t_v[11,::-1,:]
    #Plot
    axesm()
    geoshow('country')
    layer = imshow(t, 20)
    colorbar(layer, orientation='horizontal')
    title(vname + 'at TempPrsLvls=11')
    axism()
    
.. image:: image/airs_grid.png