.. _docs-meteoinfolab-numeric-stats-ttest_1samp:


************
ttest_1samp
************

.. currentmodule:: numeric.stats

.. function:: ttest_1samp(a, popmean)

    Calculate the T-test for the mean of ONE group of scores.

    This is a two-sided test for the null hypothesis that the expected value (mean) of 
    a sample of independent observations a is equal to the given population mean, popmean.
    
    :param a: (*array_like*) Sample observation.
    :param popmean: (*float*) Expected value in null hypothesis.
    
    :returns: t-statistic and p-value
    
    Examples::
    
        from mipylib.numeric import stats

        a = array([1,2,-1,2,1,-4])
        mu = 0
        r = stats.ttest_1samp(a, mu)
        print r

    Result::
    
        >>> run script...
        (0.17622684421256019, 0.8670310908282268)