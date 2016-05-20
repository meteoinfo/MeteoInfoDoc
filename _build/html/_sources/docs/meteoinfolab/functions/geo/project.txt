.. _docs-meteoinfolab-funcitons-geo-project:


*******************
project
*******************

.. function:: project(x, y, fromproj=KnownCoordinateSystems.geographic.world.WGS1984, toproj=KnownCoordinateSystems.geographic.world.WGS1984)

    Create a projection object with Proj.4 parameters.
    
    Project geographic coordinates from one projection to another.
    
    :param x: (*array_like*) X coordinate values for projection.
    :param y: (*array_like*) Y coordinate values for projection.
    :param fromproj: (*ProjectionInfo*) From projection. Default is longlat projection.
    :param toproj: (*ProjectionInfo*) To projection. Default is longlat projection.
    
    :returns: (*array_like*, *array_like*) Projected geographic coordinates.  
    
    **Example:**
    
    Project a geographic coordinate from longlat projection to Lambert projection:
    
    ::
    
        >>> fromproj = projinfo()
        >>> toproj = projinfo(proj='lcc', lon_0=104.137, lat_0=35.946, lat_1=30.0, lat_2=60.0)
        >>> lon = 104.583
        >>> lat = 35.5731
        >>> x, y = project(lon, lat, fromproj=fromproj, toproj=toproj)
        >>> x, y
        (39626.10751807479, -40422.11861349553)
        
    Project Lambert coordinates to longlat projection:
        
    ::
    
        #Add file
        fn = 'D:/Temp/grads/wrfout_d02.ctl'
        f = addfile(fn)
        #Get a variable
        v = f['T2']
        #Get X/Y dimension value - coordinates under Lambert projection
        x = v.dimvalue(2)
        y = v.dimvalue(1)
        #Project X/Y to Lon/Lat
        toproj = projinfo()    #Lon/Lat projection
        xx, yy = meshgrid(x, y)
        lon, lat = project(xx, yy, fromproj=f.proj, toproj=toproj)
        #Write lon/lat
        lon.savegrid(x, y, 'C:/Temp/test/lon.txt')
        lat.savegrid(x, y, 'C:/Temp/test/lat.txt')
        #Plot for test
        scatter(lon[::4,::4], lat[::4,::4], edge=False, size=3, color='b')