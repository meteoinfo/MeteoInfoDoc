.. _docs-meteoinfolab-dataset-midata-binwrite:


******************************************
binwrite
******************************************

.. currentmodule:: mipylib.dataset.midata

.. function:: binwrite(fn, data, byteorder='little_endian', append=False)

    Write array data into a binary data file.
    
    :param fn: (*string*) Path needed to locate binary file.
    :param data: (*array_like*) A numeric array variable of any dimensionality.
    :param byteorder: (*string*) Byte order. ``little_endian`` or ``big_endian``.
    :param append: (*boolean*) Append to an existing file or not.
    
    Examples
    
    ::
    
        fn = 'D:/Temp/grads/model.ctl'
        f = addfile(fn)
        ps = f['PS'][:,:,:]
        binwrite('D:/Temp/grads/binwrite_test.bin', ps)