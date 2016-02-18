.. _docs-meteoinfolab-funcitons-file_io-addfile:


*******************
addfile
*******************

.. function:: addfile(fname, access='r', dtype='netcdf')

    Opens a data file that is written in a supported file format.
    
    :param fname: (*string*) The full or relative path of the data file to load.
    :param access: (*string*) The access right setting to the data file. Default is ``r``.
    :param dtype: (*string*) The data type of the data file. Default is ``netcdf``.
    
    :returns: (*DimDataFile*) Opened file object.
    
    Examples
    
    ::
    
        >>> f = addfile('D:/Temp/GrADS/model.ctl')
        >>> f
        Title: 5 Days of Sample Model Output
        Descriptor: D:/Temp/GrADS/model.ctl
        Binary: D:\Temp\GrADS\model.dat
        Type = Gridded
        X Dimension: Xmin = 0.0; Xmax = 355.0; Xsize = 72; Xdelta = 5.0
        Y Dimension: Ymin = -90.0; Ymax = 90.0; Ysize = 46; Ydelta = 4.0
        Zsize = 7  Tsize = 5
        Number of Variables = 8
        PS 0 99 Surface
        U 7 99 U
        V 7 99 V
        Z 7 99 Geopotential
        T 7 99 Temperature
        Q 5 99 Specific
        TS 0 99 Surface
        P 0 99 Precipitation