.. _docs-meteoinfolab-dataset-midata-grads2nc:


******************************************
grads2nc
******************************************

.. currentmodule:: mipylib.dataset.midata

.. function:: grads2nc(infn, outfn, big_endian=None)

    Convert GrADS data file to netCDF data file.
    
    :param infn: (*string*) Input GrADS data file name.
    :param outfn: (*string*) Output netCDF data file name.
    :param big_endian: (*boolean*) Is GrADS data big_endian or not.