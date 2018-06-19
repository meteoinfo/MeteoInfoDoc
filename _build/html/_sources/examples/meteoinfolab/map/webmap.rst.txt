.. _examples-meteoinfolab-map-webmap:

***********************************
Add web map layer
***********************************

Web map layer can be added in a map axes using ``webmap`` function. Currently supported web map 
providers:

- OpenStreetMap
- OpenStreetMapQuestSattelite
- BingMap
- BingSatelliteMap
- BingHybridMap
- GoogleMap
- GoogleSatelliteMap
- GoogleTerrainMap
- GoogleHybridMap
- GoogleHybridTerrainMap
- OviMap
- OviSatelliteMap
- OviTerrainMap
- OviHybridMap
- YahooMap
- YahooSatelliteMap
- YahooHybridMap

The tile images are Mercator projection, so the map axes should be created as Mercator projection.

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
    
.. image:: ../../../_static/webmap_1.png