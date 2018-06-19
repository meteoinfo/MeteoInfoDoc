.. _docs-meteoinfolab-dataset-midata-ncwrite:


******************************************
ncwrite
******************************************

.. currentmodule:: mipylib.dataset.midata

.. function:: ncwrite(fn, data, varname, dims=None, attrs=None)

    Write a netCDF data file from an array.
    
    :param: fn: (*string*) netCDF data file path.
    :param data: (*array_like*) A numeric array variable of any dimensionality.
    :param varname: (*string*) Variable name.
    :param dims: (*list of dimensions*) Dimension list.
    :param attrs: (*list of attributes*) Attributes list.
    
    Examples
    
    ::
    
        fn = 'D:/Temp/grads/model.ctl'
        f = addfile(fn)
        ps = f['PS'][:,:,:]
        ncwrite('D:/Temp/grads/ncwrite_test.nc', ps, 'PS')