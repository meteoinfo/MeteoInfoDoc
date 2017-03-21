.. _docs-meteoinfolab-numeric-stats-cov:


**********
cov
**********

.. currentmodule:: numeric.stats

.. function:: cov(m, y=None, rowvar=True, bias=False)

    Estimate a covariance matrix.
    
    :param m: (*array_like*) A 1-D or 2-D array containing multiple variables and observations.
    :param y: (*array_like*) Optional. An additional set of variables and observations. y has the same form as 
        that of m.
    :param rowvar: (*boolean*) If ``rowvar`` is True (default), then each row represents a variable, with 
        observations in the columns. Otherwise, the relationship is transposed: each column represents a 
        variable, while the rows contain observations.
    :param bias: (*boolean*) Default normalization (False) is by (N - 1), where N is the number of observations 
        given (unbiased estimate). If bias is True, then normalization is by N.
    
    :returns: Covariance.
    
    Examples::
    
        from mipylib.numeric import stats

        x1 = [12, 2, 1, 12, 2]
        x2 = [1, 4, 7, 1, 0]
        c = stats.cov(x1, x2)
        print c

        x = array([[0, 2], [1, 1], [2, 0]]).T
        print stats.cov(x)

        x = array([[12, 2, 1, 12, 2], [1, 4, 7, 1, 0]])
        print stats.cov(x)
        print stats.cov(x, x)

    Result::
    
        >>> run script...
        array([[32.2, -9.1]
              [-9.1, 8.3]])
        array([[1.0, -1.0]
              [-1.0, 1.0]])
        array([[32.2, -9.1]
              [-9.1, 8.3]])
        array([[32.2, -9.1, 32.2, -9.1]
              [-9.1, 8.3, -9.1, 8.300000000000002]
              [32.2, -9.1, 32.2, -9.1]
              [-9.1, 8.300000000000002, -9.1, 8.3]])