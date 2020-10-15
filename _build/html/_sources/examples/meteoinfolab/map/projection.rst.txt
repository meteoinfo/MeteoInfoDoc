.. _examples-meteoinfolab-map-projection:

*******************
Map projection
*******************

Map projection can be set when creating a map axes using **axesm** function by **projinfo** 
parameter. Projection object can be created using **projinfo** function with Proj4 style 
parameters (ref: http://remotesensing.org/geotiff/proj_list ). **axism** function is used
to set projected map extent with a list parameter including start and end longtitudes
and start and end latitudes.

::

    #Plot
    proj = projinfo(proj='lcc', lon_0=105, lat_1=25, lat_2=47)
    axesm(projinfo=proj, axison=False)
    geoshow('cn_province', edgecolor='lightgray')
    geoshow('cn_border', facecolor=(0,0,255))
    ss = makesymbolspec('line', {'value':'Yangtze', 'color':(0,255,255), 'size':1}, \
        {'value':'Huang He', 'color':(0,255,255), 'size':1}, field='NAME')
    geoshow('rivers', symbolspec=ss)
    geoshow('cn_cities', facecolor='r', size=4, labelfield='NAME', fontname=u'楷体', \
        fontsize=16, yoffset=15)
    axism([78, 130, 14, 53])
        
.. image:: ../../../_static/map_projection.png