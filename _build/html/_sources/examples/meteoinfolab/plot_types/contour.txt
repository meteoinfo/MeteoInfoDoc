.. _examples-meteoinfolab-plot_types-contour:

*******************
Contour plot
*******************

Contour plot was created by ``contour()`` function. ``contourf()`` function is for filled
contour plot.

::

    f = addfile('D:/Temp/nc/cone.nc')
    u = f['u'][4,:,:]
    subplot(2,1,1)
    layer = contour(u)
    clabel(layer)
    title('Cone amplitude')
    colorbar(layer)

    subplot(2,1,2)
    u = f['u'][5,:,:]
    layer = contourf(u)
    title('Cone amplitude')
    colorbar(layer)
    
.. image:: ../../../_static/contour.png

Corresponding functions for map plot are ``contourm()`` and ``contourfm()`` .

::

    f = addfile('D:/Temp/GrADS/model.ctl')
    psv = f['PS']
    ps = psv[0,'10:60','60:140']
    axesm()
    mlayer = shaperead('D:/Temp/map/country1.shp')
    geoshow(mlayer, edgecolor=(0,0,255))
    #layer = contourm(ps, 20)
    layer = contourfm(ps, 20)
    title('Pressure')
    yticks(arange(20, 61, 20))
    grid()
    colorbar(layer, orientation='horizontal', extendrect=False, shrink=0.8, aspect=12)
    
.. image:: ../../../_static/contourm.png