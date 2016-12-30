.. _examples-meteoinfolab-map-add_map_layer:

*******************
Add map layer
*******************

Shape file is widely used GIS data format and there are many free online resouces. **shaperead** function is
used to read shape file as a MILayer object with map coordinates and attribution data. The object can be
added in an Axesm by **geoshow** function. A deault legend was defined when read shape file as a layer 
and it can be changed in **geoshow** function by setting **facecolor**, **edgecolor**, **size** and so on parameters.
Also a more complex legen can be created using 'makesymbolspec' function. Following code will create a legend
with two breaks of Yangtze and Huang He rivers.

::

    ss = makesymbolspec('line', {'value':'Yangtze', 'color':(0,255,255), 'size':1}, \
        {'value':'Huang He', 'color':(0,255,255), 'size':1}, field='NAME')
    geoshow(river_layer, symbolspec=ss)
    
If a point layer was added, 'labelfield' and other associated parameters can be used to add labels to points.

::

    #Set data folders
    basedir = 'D:/MyProgram/Distribution/java/MeteoInfo/MeteoInfo'
    mapdir = os.path.join(basedir, 'map')
    #Read shape files
    bou2_layer = shaperead(os.path.join(mapdir, 'bou2_4p.shp'))
    bou1_layer = shaperead(os.path.join(mapdir, 'bou1_4l.shp'))
    river_layer = shaperead(os.path.join(mapdir, 'rivers.shp'))
    city_layer = shaperead(os.path.join(mapdir, 'res1_4m.shp'))
    #Plot
    axesm()
    geoshow(bou2_layer, edgecolor='lightgray')
    geoshow(bou1_layer, facecolor=(0,0,255))
    ss = makesymbolspec('line', {'value':'Yangtze', 'color':(0,255,255), 'size':1}, \
        {'value':'Huang He', 'color':(0,255,255), 'size':1}, field='NAME')
    geoshow(river_layer, symbolspec=ss)
    geoshow(city_layer, facecolor='r', size=4, labelfield='NAME', fontname=u'楷体', fontsize=16, yoffset=15)
    xlim(72, 136)
    ylim(16, 55)
    
.. image:: image/add_map_layer.png