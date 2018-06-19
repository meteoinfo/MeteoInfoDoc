.. _docs-meteoinfolab-numeric-stats-covariance:


**********
covariance
**********

.. currentmodule:: numeric.stats

.. function:: covariance(x, y, bias=False)

    Calculate covariance of two array.
    
    :param x: (*array_like*) A 1-D array containing multiple variables and observations.
    :param y: (*array_like*) An additional set of variables and observations. y has the same form as 
        that of x.
    :param bias: (*boolean*) Default normalization (False) is by (N - 1), where N is the number of observations 
        given (unbiased estimate). If bias is True, then normalization is by N.
        
    returns: Covariance
    
    Examples::
    
        from mipylib.numeric import stats

        x1 = [12, 2, 1, 12, 2]
        x2 = [1, 4, 7, 1, 0]
        c = stats.cov(x1, x2)
        print c

    Result::
    
        >>> run script...
        -7.28