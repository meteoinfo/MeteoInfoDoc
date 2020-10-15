.. _examples-meteoinfolab-map-image_layer:

*******************
Add image layer
*******************

Image file formats of jpeg, png, bmp and gif can be loaded as image layer using ``georead()``
function, and the image can be geo-located by creating geo-location file with the image file.

::

    fn = os.path.join(migl.get_sample_folder(), 'GrADS', 'model.ctl')
    f = addfile(fn)
    ps = f['PS'][0,'10:60','70:140']
    imfn = os.path.join(migl.get_map_folder(), 'global_shade.jpg')
    lrelief = georead(imfn)

    #Plot
    axesm()
    geoshow(lrelief)
    geoshow('country', edgecolor=[0,0,255])
    layer = contourf(ps, edgecolor='gray', zorder=1, alpha=0.5)
    title('Pressure')
    colorbar(layer, aspect=20)
        
.. image:: ../../../_static/image_layer.png