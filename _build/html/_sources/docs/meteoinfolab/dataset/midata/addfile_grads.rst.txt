.. _docs-meteoinfolab-dataset-midata-addfile_grads:


*****************************
addfile_grads
*****************************

.. currentmodule:: mipylib.dataset.midata

.. function:: addfile_grads(fname, getfn=True)

    Add a GrADS data file. use this function is GrADS control file has no ``.ctl`` suffix, otherwise use
    ``addfile`` function.
    
    :param fname: (*string*) GrADS control file name.
    :param getfn: (*string*) If run ``__getfilename`` function or not. Default is ``True``.
    
    :returns: (*DimDataFile*) Opened file object.    