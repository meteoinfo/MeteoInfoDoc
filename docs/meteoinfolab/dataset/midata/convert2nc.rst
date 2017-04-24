.. _docs-meteoinfolab-dataset-midata-convert2nc:


******************************************
convert2nc
******************************************

.. currentmodule:: mipylib.dataset.midata

.. function:: convert2nc(infn, outfn, version='netcdf3')

    Convert data file (Grib, HDF...) to netCDF data file.
    
    :param infn: (*string*) Input data file name.
    :param outfn: (*string*) Output netCDF data file name.
    
    Examples
    
    ::
    
        infn = 'D:/Temp/grib/C1D01010000010109001'    #Input GRIB file
        outfn = 'D:/Temp/grib/C1D01010000010109001.nc'    #Output netCDF file
        convert2nc(infn, outfn)