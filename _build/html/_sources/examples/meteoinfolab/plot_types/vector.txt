.. _examples-meteoinfolab-plot_types-vector:

*******************
Vector plot
*******************

Vector plot was created by ``quiver()`` or ``quiverm()`` (for map axes) function. ``quiverkey`` function
can be used to add a key in a quiver plot.

::

    f = addfile('D:/Temp/GrADS/model.ctl')
    u = f['U'][0,[500],[10,60],[60,140]]
    v = f['V'][0,[500],[10,60],[60,140]]
    speed = sqrt(u*u+v*v)
    #Plot
    axesm()
    lworld = shaperead('D:/Temp/Map/country1.shp')
    geoshow(lworld)
    layer = quiverm(u, v, speed, 10, size=8)
    quiverkey(layer, 0.74, 0.18, 15, bbox={'edge':True, 'fill':True})
    colorbar(layer)
    title('Wind field')
    yticks([20,40,60])
    
.. image:: ../../../_static/vector.png