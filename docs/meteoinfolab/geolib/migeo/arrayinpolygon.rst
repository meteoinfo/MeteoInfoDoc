.. _docs-meteoinfolab-geolib-migeo-arrayinpolygon:


*********************************
arrayinpolygon
*********************************

.. currentmodule:: mipylib.geolib.migeo

.. function:: arrayinpolygon(a, polygon, x=None, y=None)
    
    Set array element value as 1 if inside a polygon or set value as -1.
    
    :param a: (*array_like*) The array.
    :param polygon: (*PolygonShape*) The polygon.
    :param x: (*float*) X coordinate of the point. Default is ``None``, for DimArray
    :param y: (*float*) Y coordinate of the point. Default is ``None``, for DimArray
    
    :returns: (*array_like*) Result array.