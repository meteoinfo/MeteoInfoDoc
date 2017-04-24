.. _docs-meteoinfolab-dataset-midata-addfile_hyconc:


**************************************
addfile_hyconc
**************************************

.. currentmodule:: mipylib.dataset.midata

.. function:: addfile_hyconc(fname, getfn=True)

    Add a HYSPLIT concentration data file.
    
    :param fname: (*string*) The HYSPLIT concentration file name.
    :param getfn: (*string*) If run ``__getfilename`` function or not. Default is ``True``.
    
    :returns: (*DimDataFile*) Opened file object.