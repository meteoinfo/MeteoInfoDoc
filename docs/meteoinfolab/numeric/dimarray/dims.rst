.. _docs-meteoinfolab-numeric-dimarray-DimArray-dims:


*******************
dims
*******************

.. attribute:: DimArray.dims

    Return a dimension list of the DimArray object.
    
    Examples::

        >>> f = addfile_hyconc('C:/hysplit4/working/cdump')
        >>> data = f['TEST'][0,0,:,:]
        >>> data.dims
        [Name: lat
            Min value: 25.0
            Max value: 55.0
            Size: 601
            Delta: 0.05, 
        Name: lon
            Min value: -105.0
            Max value: -75.0
            Size: 601
            Delta: 0.05]