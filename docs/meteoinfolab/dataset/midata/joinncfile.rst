.. _docs-meteoinfolab-dataset-midata-joinncfile:


*********************************************
joinncfile
*********************************************

.. currentmodule:: mipylib.dataset.midata

.. function:: joinncfile(infns, outfn, tdimname)

    Join several netCDF files to one netCDF file.
    
    :param infns: (*list*) Input netCDF file name list.
    :param outfn: (*string*) Output netCDF file name.
    :param tdimname: (*string*) Time dimension name.
    
    :returns: Joined netCDF file.