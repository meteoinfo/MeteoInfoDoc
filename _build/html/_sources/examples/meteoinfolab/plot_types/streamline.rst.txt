.. _examples-meteoinfolab-plot_types-streamline:

*******************
Streamline plot
*******************

Streamline plot was created by ``streamplot()`` function.

::

    fn = os.path.join(migl.get_sample_folder(), 'GrADS', 'model.ctl')
    f = addfile(fn)
    u = f['U'][0,'500','10:60','60:140']
    v = f['V'][0,'500','10:60','60:140']
    
    #Plot
    axesm()
    geoshow('country', edgecolor='k')
    layer = streamplotm(u, v)
    title('Streamline plot example')
    yticks([20,40,60])
    
.. image:: ../../../_static/streamline.png