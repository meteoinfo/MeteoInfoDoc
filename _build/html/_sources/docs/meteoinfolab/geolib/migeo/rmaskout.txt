.. _docs-meteoinfolab-geolib-migeo-rmaskout:


*********************************
rmaskout
*********************************

.. currentmodule:: mipylib.geolib.migeo

.. function:: rmaskout(data, x, y, mask)
    
    Maskout data by polygons - the elements outside polygons will be removed
    
    :param data: (*array_like*) Array data for maskout.
    :param x: (*array_like*) X coordinate array.
    :param y: (*array_like*) Y coordinate array.
    :param mask: (*list*) Polygon list as maskout borders.
    
    :returns: (*list*) Maskouted data, x and y array list.