.. _docs-meteoinfolab-geolib-migeo-georead:


*********************************************
georead
*********************************************

.. currentmodule:: mipylib.geolib.migeo

.. function:: georead(fn)

    Returns a layer readed from a supported geo-data file.
    
    :param fn: (*string*) The supported geo-data file name (shape file, wmp, geotiff, image, bil...).
    
    :returns: (*MILayer*) The created layer.
    
    Examples::
    
        f = addfile('D:/Temp/GrADS/model.ctl')
        ps = f['PS'][0,[10,60],[70,140]]
        lrelief = georead('D:/Temp/Map/GLOBALeb3colshade.jpg')
        world = georead('D:/Temp/Map/country1.shp')
        axesm()
        geoshow(lrelief)
        geoshow(world, edgecolor=[0,0,255])
        cols = makecolors(20, alpha=128)
        layer = contourfm(ps, colors=cols, edgecolor='gray', order=1)
        title('Pressure')
        colorbar(layer, aspect=12)
            
    .. image:: ../../../../_static/image_layer.png