.. _docs-meteoinfolab-dataset-midata-addfile:


*******************
addfile
*******************

.. currentmodule:: mipylib.dataset.midata

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
        File Name: D:/Temp/GrADS/model.ctl
        Dimensions: 5
            X = 72;
            Y = 46;
            Z = 7;
            T = 5;
            Z_5 = 5;
        X Dimension: Xmin = 0.0; Xmax = 355.0; Xsize = 72; Xdelta = 5.0
        Y Dimension: Ymin = -90.0; Ymax = 90.0; Ysize = 46; Ydelta = 4.0
        Global Attributes: 
            : data_format = "GrADS binary"
            : fill_value = -2.56E33
            : title = "5 Days of Sample Model Output"
        Variations: 8
            float PS(T,Y,X);
                PS: description = "Surface"
            float U(T,Z,Y,X);
                U: description = "U"
            float V(T,Z,Y,X);
                V: description = "V"
            float Z(T,Z,Y,X);
                Z: description = "Geopotential"
            float T(T,Z,Y,X);
                T: description = "Temperature"
            float Q(T,Z_5,Y,X);
                Q: description = "Specific"
            float TS(T,Y,X);
                TS: description = "Surface"
            float P(T,Y,X);
                P: description = "Precipitation"