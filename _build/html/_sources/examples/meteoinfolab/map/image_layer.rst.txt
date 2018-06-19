.. _examples-meteoinfolab-map-image_layer:

*******************
Add image layer
*******************

Image file formats of jpeg, png, bmp and gif can be loaded as image layer using ``georead()``
function, and the image can be geo-located by creating geo-location file with the image file.

::

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
        
.. image:: ../../../_static/image_layer.png