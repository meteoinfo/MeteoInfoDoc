.. _docs-meteoinfolab-geolib-migeo-polygon:


*********************************
polygon
*********************************

.. currentmodule:: mipylib.geolib.migeo

.. function:: polygon(x, y = None)

    Create polygon from coordinate data.
    
    :param x: (*array_like*) X coordinate array. If y is ``None``, x should be 2-D array contains x and y.
    :param y: (*array_like*) Y coordinate array.
    
    :returns: (*PolygonShape*) Created polygon.