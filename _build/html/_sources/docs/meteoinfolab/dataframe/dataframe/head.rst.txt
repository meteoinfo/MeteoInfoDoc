.. _docs-meteoinfolab-dataframe-dataframe-DataFrame-head:


*******************
head
*******************

.. method:: DataFrame.head(n=5)

    Get top rows
        
    :param n: (*int*) row number.
        
    :returns: Top rows
    
    Examples::

        >>> df = DataFrame({'animal':['alligator', 'bee', 'falcon', 'lion',
        ...                    'monkey', 'parrot', 'shark', 'whale', 'zebra']})
        >>> df
              animal
        0  alligator
        1        bee
        2     falcon
        3       lion
        4     monkey
        5     parrot
        6      shark
        7      whale
        8      zebra
        
    Viewing the first 5 lines::
    
        >>> df.head()
              animal
        0  alligator
        1        bee
        2     falcon
        3       lion
        4     monkey
        
    Viewing the first `n` lines (three in this case)::
    
        >>> df.head(3)
              animal
        0  alligator
        1        bee
        2     falcon