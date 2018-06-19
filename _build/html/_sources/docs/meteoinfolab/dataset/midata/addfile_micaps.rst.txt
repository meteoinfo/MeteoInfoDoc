.. _docs-meteoinfolab-dataset-midata-addfile_micaps:


*****************************
addfile_micaps
*****************************

.. currentmodule:: mipylib.dataset.midata

.. function:: addfile_micaps(fname, getfn=True)

    Add a MICAPS data file (Data formats from CMA).
    
    :param fname: (*string*) The MICAPS file name.
    :param getfn: (*string*) If run ``__getfilename`` function or not. Default is ``True``.
    
    :returns: (*DimDataFile*) Opened file object.