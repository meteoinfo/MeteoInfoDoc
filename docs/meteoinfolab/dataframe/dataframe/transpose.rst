.. _docs-meteoinfolab-dataframe-dataframe-DataFrame-transpose:


*******************
transpose
*******************

.. method:: DataFrame.transpose()

    Transpose data frame.
        
    :returns: Transposed data frame.
    
    Examples::

        >>> d1 = {'col1': [1, 2], 'col2': [3, 4]}
        >>> df1 = DataFrame(data=d1)
        >>> df1
           col1  col2
        0     1     3
        1     2     4
        
        >>> df1_transposed = df1.T # or df1.transpose()
        >>> df1_transposed
              0  1
        col1  1  2
        col2  3  4