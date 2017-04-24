.. _docs-meteoinfolab-geolib-migeo-maskout:


*********************************
maskout
*********************************

.. currentmodule:: mipylib.geolib.migeo

.. function:: maskout(data, mask, x=None, y=None)
    
    Maskout data by polygons - NaN values of elements outside polygons.
    
    :param mask: (*list*) Polygon list as maskout borders.
    :param data: (*array_like*) Array data for maskout.
    :param x: (*array_like*) X coordinate array.
    :param y: (*array_like*) Y coordinate array.

    :returns: (*array_like*) Maskouted data array.