.. _examples-meteoinfolab-map-ave_polygons:

***********************************
Average data in each polygon
***********************************

Array data can be masked using polygons, then statistical values of the polygons can be obtained using the masked array.
Below script will get average, min, max temporature of each state in US.

::

    #Add a surfer grid data 
    f = addfile_surfer('D:/Temp/ascii/usgrid.dat') 
    tdata = f['var'][:,:] 
    #Read US shape file 
    us = shaperead('D:/Temp/map/states.shp') 
    #Average temporature for each state 
    i = 0 
    for rpoly in us.shapes(): 
        name = us.cellvalue('STATE_NAME', i) 
        mdata = tdata.maskout(rpoly) 
        tave = mdata.ave() 
        tmin = mdata.min() 
        tmax = mdata.max() 
        print name + ', Ave: %.2f, Min: %.2f, Max: %.2f' %(tave, tmin, tmax) 
        i += 1 

    #Plot 
    axesm() 
    world = shaperead('D:/Temp/map/country1.shp') 
    geoshow(world) 
    geoshow(us, edgecolor=[0,0,255]) 
    layer = contourfm(tdata,20) 
    title('Temporature distribution map') 
    colorbar(layer)
    
.. image:: ../../../_static/ave_polygons.png