.. _docs-meteoinfolab-dataframe-dataframe-DataFrame-append:


*******************
append
*******************

.. method:: DataFrame.append(other)

    Append another data frame.
        
    :param other: (*DataFrame*) Other data frame.
        
    :returns: (*DataFrame*) Appended data frame.
    
    Examples::

        >>> df = DataFrame(array([[1, 2], [3, 4]]), columns=list('AB'))
        >>> df
          A B
        0 1 2
        1 3 4
        >>> df2 = DataFrame(array([[5, 6], [7, 8]]), columns=list('AB'))
        >>> df2
          A B
        0 5 6
        1 7 8
        >>> df.append(df2)
          A B
        0 1 2
        1 3 4
        0 5 6
        1 7 8