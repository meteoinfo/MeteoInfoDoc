.. _docs-meteoinfolab-dataframe-dataframe-DataFrame-shape:


*******************
shape
*******************

.. attribute:: DataFrame.shape

    Return a tuple representing the dimensionality of the DataFrame.
    
    Examples::

        >>> df = DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.shape
        (2, 2)