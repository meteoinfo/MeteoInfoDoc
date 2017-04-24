.. _docs-meteoinfolab-dataset-midata-addfile_awx:


*****************************
addfile_awx
*****************************

.. currentmodule:: mipylib.dataset.midata

.. function:: addfile_awx(fname, getfn=True)

    Add a AWX data file (Satellite data file format from CMA). use this function is the file has no ``.awx`` 
    suffix, otherwise use ``addfile`` function.
    
    :param fname: (*string*) The AWX file name.
    :param getfn: (*string*) If run ``__getfilename`` function or not. Default is ``True``.
    
    :returns: (*DimDataFile*) Opened file object.    