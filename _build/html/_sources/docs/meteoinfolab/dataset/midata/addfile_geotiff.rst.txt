.. _docs-meteoinfolab-dataset-midata-addfile_geotiff:


*****************************
addfile_geotiff
*****************************

.. currentmodule:: mipylib.dataset.midata

.. function:: addfile_geotiff(fname, getfn=True)

    Add a Geotiff data file.
    
    :param fname: (*string*) The Geotiff file name.
    :param getfn: (*string*) If run ``__getfilename`` function or not. Default is ``True``.
    
    :returns: (*DimDataFile*) Opened file object.