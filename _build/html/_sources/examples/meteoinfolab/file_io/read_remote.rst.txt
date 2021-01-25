.. _examples-meteoinfolab-file_io-read_remote:

***********************************
Read remote data
***********************************

Remote data on OpenDAP, ADDE and THREDDS server can be read using ``addfile()`` function similar with local
data files.

::

    fn = 'http://monsoondata.org:9090/dods/model'
    f = addfile(fn)
    v = f['ps']
    ps = v[0,:,:]
    #Plot
    axesm(tickfontsize=12)
    geoshow('country')
    layer = contourf(ps, 20)
    colorbar(layer, orientation='horizontal', fontsize=12)
    title(fn)
    
.. image:: ../../../_static/read_remote.png

::

    fn = 'https://eosdap.hdfgroup.org:8080/opendap/data/NASAFILES/hdf5/OMI-Aura_L3-OMTO3d_2009m0102_v003-2009m0602t151018.he5'
    f = addfile(fn)
    vname = 'RadiativeCloudFraction'
    data = f[vname][:,:]
    #Plot
    axesm()
    geoshow('country')
    layer = imshow(data, 20)
    colorbar(layer, orientation='horizontal')
    title(vname)
    
.. image:: ../../../_static/read_remote_2.png