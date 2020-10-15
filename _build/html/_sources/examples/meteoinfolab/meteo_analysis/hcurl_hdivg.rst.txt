.. _examples-meteoinfolab-meteo_analysis-hcurl_hdivg:

*******************
Vorticity and divergence
*******************

Calculate vorticity and divergence from u and v wind components using ``hcurl()`` and 
``hdivg()`` functions.

::

    f = addfile('D:/Temp/GrADS/model.ctl')
    u = f['U'][0,0,:,:]
    v = f['V'][0,0,:,:]
    vort = hcurl(u, v)
    divg = hdivg(u, v)

    subplot(2,1,1,axestype='map')
    geoshow('country')
    layer = contourf(vort, 20)
    title('Vorticity')
    colorbar(layer, orientation='horizontal', aspect=50)

    subplot(2,1,2,axestype='map')
    geoshow('country')
    layer = contourf(divg, 20)
    title('Divergence')
    colorbar(layer, orientation='horizontal', aspect=50)
    
.. image:: image/hcurl_hdivg.png