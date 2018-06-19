.. _docs-meteoinfolab-dataset-midata-addfile_hytraj:


***********************************
addfile_hytraj
***********************************

.. currentmodule:: mipylib.dataset.midata

.. function:: addfile_hytraj(fname, getfn=True)

    Add a HYSPLIT trajectory endpoint data file.
    
    :param fname: (*string*) The HYSPLIT trajectory endpoint file name.
    :param getfn: (*string*) If run ``__getfilename`` function or not. Default is ``True``.
    
    :returns: (*DimDataFile*) Opened file object.