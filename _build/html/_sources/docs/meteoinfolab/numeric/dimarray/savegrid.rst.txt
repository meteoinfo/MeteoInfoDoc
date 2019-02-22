.. _docs-meteoinfolab-numeric-dimarray-DimArray-savegrid:


*******************
savegrid
*******************

.. method:: DimArray.savegrid(fname, format='surfer', **kwargs)

    Save the array data to an ASCII or binary file. The array must be 2 dimension.
        
    :param fname: (*string*) File name.
    :param format: (*string*) File format [surfer | bil | esri_ascii | micaps4].
    :param description: (*string*) Data description - only used for ``micaps4`` file.
    :param date: (*datetime*) Data datetime - only used for ``micaps4`` file.
    :param hours: (*int*) Data forcasting hours - only used for ``micaps4`` file.
    :param level: (*float*) Data vertical level - only used for ``micaps4`` file.
    :param smooth: (*int*) 1 or 0 - only used for ``micaps4`` file.
    :param boldvalue: (*int*) Bold contour value - only used for ``micaps4`` file.
    :param proj: (*ProjectionInfo*) Data ProjectionInfo - only used for ``micaps4`` file.
    :param float_format: (*string*) Float number format, such as '%.2f'.
    
    Examples::

        >>> data.savegrid('C:/Temp/test.txt', float_format='%.2f')