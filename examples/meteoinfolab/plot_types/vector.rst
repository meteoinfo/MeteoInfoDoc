.. _examples-meteoinfolab-plot_types-vector:

*******************
Vector plot
*******************

Vector plot was created by ``quiver()`` function. ``quiverkey`` function
can be used to add a key in a quiver plot.

::

    fn = os.path.join(migl.get_sample_folder(), 'GrADS', 'model.ctl')
    f = addfile(fn)
    u = f['U'][0,'500','10:60','60:140']
    v = f['V'][0,'500','10:60','60:140']
    speed = sqrt(u*u+v*v)
    #Plot
    axesm()
    geoshow('country')
    layer = quiver(u, v, speed, 10, size=8)
    quiverkey(layer, 0.74, 0.18, 15, bbox={'edge':True, 'fill':True})
    colorbar(layer)
    title('Wind field')
    yticks([20,40,60])
    
.. image:: ../../../_static/vector.png