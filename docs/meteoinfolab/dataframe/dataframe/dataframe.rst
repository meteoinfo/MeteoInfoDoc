.. _docs-meteoinfolab-dataframe-dataframe-DataFrame:


*********************************
DataFrame
*********************************

.. currentmodule:: mipylib.dataframe.dataframe

.. class:: DataFrame

    Two-dimensional size-mutable, potentially heterogeneous tabular data structure with 
    labeled axes (rows and columns). Arithmetic operations align on both row and column 
    labels. Can be thought of as a dict-like container for Series objects.
    
    :param data: (*array_like*) Two-dimensional array data or list of one-dimensional arrays.
    :param index: (*list*) Data index list. Values must be unique and hashable, same length as data.
    :param columns: (*list*) Column labels to use for resulting frame. Will default to 
        arange(n) if no column labels are provided
    

Attributes:
------------

.. toctree::
   :maxdepth: 1
   
   shape.rst
   dtypes.rst
    
Methods:
----------

.. toctree::
   :maxdepth: 1

   append.rst
   head.rst
   read_table.rst
   tail.rst
   to_csv.rst
   transpose.rst   