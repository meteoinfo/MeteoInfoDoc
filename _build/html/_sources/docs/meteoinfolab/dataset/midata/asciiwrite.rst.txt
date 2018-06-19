.. _docs-meteoinfolab-dataset-midata-asciiwrite:


*****************************
asciiwrite
*****************************

.. currentmodule:: mipylib.dataset.midata

.. function:: asciiwrite(fn, data, colnum=80, format=None, delimiter=None)

    Write array data into a ASCII data file.
    
    :param fn: (*string*) Path needed to locate ASCII file.
    :param data: (*array_like*) A numeric array variable of any dimensionality.
    :param colnum: (*int*) Column number of each line.
    :param format: (*string*) Number format.
    :param delimiter: (*string*) Delimiter string. 
    
    Examples
    
    ::
    
        f = addfile('D:/Temp/GrADS/model.ctl')
        data = f['PS'][0,:,:]
        asciiwrite('C:/Temp/test/test_asciisave.txt', data, format='%-10.2f')