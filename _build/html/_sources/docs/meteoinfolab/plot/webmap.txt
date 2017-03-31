.. _docs-meteoinfolab-funcitons-plot-webmap:


*******************
webmap
*******************

.. function:: webmap(provider='OpenStreetMap', order=0)

    Add a new web map layer.
    
    :param provider: (*string*) Web map provider.
    :param order: (*int*) Layer order.
    
    :returns: Web map layer
    
    **Example:**
    
    ::

        #Add a map axes with mercator projection 
        axesm(position=[0,0,1,1], proj='merc', griddx=5, griddy=5)
        #Add a web map layer
        wlayer = webmap(provider='BingHybridMap')
        #Add a shape layer
        lchina = shaperead('D:/Temp/Map/bou2_4p.shp')
        geoshow(lchina, edgecolor='b')
        #Set lon/lat extent
        axism([110, 130, 35, 45])
        title('Web map example')
        
    .. image:: ../../../../_static/webmap_1.png