.. _docs-meteoinfolab-dataframe-dataframe-DataFrame-tail:


*******************
tail
*******************

.. method:: DataFrame.tail(n=5)

    Get bottom rows
        
    :param n: (*int*) row number.
     
    :returns: Bottom rows
    
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
        
    Viewing the last 5 lines::
    
        >>> df.tail()
              animal
        4     monkey
        5     parrot
        6      shark
        7      whale
        8      zebra
        
    Viewing the first `n` lines (three in this case)::
    
        >>> df.tail(3)
              animal
        6      shark
        7      whale
        8      zebra