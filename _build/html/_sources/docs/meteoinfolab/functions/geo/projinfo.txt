.. _docs-meteoinfolab-funcitons-geo-projinfo:


*******************
projinfo
*******************

.. function:: projinfo(proj='longlat', **kwargs)

    Create a projection object with Proj.4 parameters.
    
    :param proj: (*string*) Projection name.
    :param lat_0: (*float*) Latitude of origin.
    :param lon_0: (*float*) Central meridian.
    :param lat_1: (*float*) Latitude of first standard paralle.
    :param lat_2: (*float*) Latitude of second standard paralle.
    :param lat_ts: (*float*) Latitude of true scale.
    :param k: (*float*) Scaling factor.
    :param x_0: (*float*) False easting.
    :param y_0: (*float*) False northing.
    :param h: (*float*) Height from earth surface.
    
    :returns: (*ProjectionInfo*) ProjectionInfo object.
    
    **Reference:**
    
    http://proj4.org/
    
    http://remotesensing.org/geotiff/proj_list/    
    
    **Example:**
    
    ::
    
        >>> proj = projinfo()
        >>> proj
        +title=long/lat:WGS84 +proj=longlat +ellps=WGS84 +datum=WGS84 +units=degrees
        >>> proj = projinfo(proj='lcc', lon_0=105, lat_1=25, lat_2=47)
        >>> proj
        +proj=lcc +lat_0=0 +lon_0=105 +lat_1=25 +lat_2=47 +lat_ts=0 +k=1 +x_0=0 +y_0=0 +h=0