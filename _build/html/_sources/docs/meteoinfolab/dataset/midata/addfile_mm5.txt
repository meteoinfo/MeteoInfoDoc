.. _docs-meteoinfolab-dataset-midata-addfile_mm5:


*****************************
addfile_mm5
*****************************

.. currentmodule:: mipylib.dataset.midata

.. function:: addfile_mm5(fname, getfn=True)

    Add a MM5 data file.
    
    :param fname: (*string*) The MM5 file name.
    :param getfn: (*string*) If run ``__getfilename`` function or not. Default is ``True``.
    
    :returns: (*DimDataFile*) Opened file object.