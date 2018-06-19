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
    mlayer = shaperead('D:/Temp/map/country1.shp')
    subplot(2,1,1)
    axesm()
    geoshow(mlayer)
    layer = contourfm(vort, 20)
    title('Vorticity')
    colorbar(layer, orientation='horizontal', aspect=50)
    subplot(2,1,2)
    axesm()
    geoshow(mlayer)
    layer = contourfm(divg, 20)
    title('Divergence')
    colorbar(layer, orientation='horizontal', aspect=50)
    
.. image:: image/hcurl_hdivg.png