.. _docs-meteoinfolab-dataset-midata-addtimedim:


*******************************************
addtimedim
*******************************************

.. currentmodule:: mipylib.dataset.midata

.. function:: addtimedim(infn, outfn, t, tunit='hours')

    Add a time dimension to a netCDF data file.
    
    :param infn: (*string*) Input netCDF file name.
    :param outfn: (*string*) Output netCDF file name.
    :param t: (*datetime*) A time value.
    :param tunit: (*string*) Time unite, Default is ``hours``.
    
    :returns: The new netCDF with time dimension.